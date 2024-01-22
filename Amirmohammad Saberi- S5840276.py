
import numpy as np
import random
import matplotlib.pyplot as plt

class Gridworld:
    def __init__(self):
        self.width = 5
        self.height = 5
        self.states = [(x, y) for x in range(self.width) for y in range(self.height)]
        self.state_values = {s: 0 for s in self.states}
        self.policy = {s: {'N': 0.25, 'S': 0.25, 'E': 0.25, 'W': 0.25} for s in self.states}
        self.gamma = 0.9  # Discount factor
        self.rewards = {s: 0 for s in self.states}  # Default reward is 0

        # Set the rewards and transitions for special states A and B
        self.rewards[(1, 0)] = 10  # A
        self.rewards[(3, 0)] = 5   # B

    def take_action(self, state, action):
        if action == 'N':
            next_state = (state[0], min(state[1]+1, self.height-1))
        elif action == 'S':
            next_state = (state[0], max(state[1]-1, 0))
        elif action == 'E':
            next_state = (min(state[0]+1, self.width-1), state[1])
        elif action == 'W':
            next_state = (max(state[0]-1, 0), state[1])

        # Check for special transitions
        if state == (1, 0):  # A
            next_state = (1, 4)  # A'
        elif state == (3, 0):  # B
            next_state = (3, 2)  # B'

        reward = self.rewards[state] if state in [(1, 0), (3, 0)] else -1 if next_state == state else 0
        return reward, next_state

class GridworldMonteCarlo(Gridworld):
    def generate_episode(self):
        episode = []
        state = random.choice(self.states)  # start from a random state
        while True:
            action_probs = self.policy[state]
            action = random.choices(list(action_probs.keys()), list(action_probs.values()))[0]
            reward, next_state = self.take_action(state, action)
            episode.append((state, action, reward))
            if next_state == state:  # episode ends if no movement
                break
            state = next_state
        return episode

    def monte_carlo_evaluation(self, episodes=1000):
        returns = {s: [] for s in self.states}  # Initialize returns for each state

        for _ in range(episodes):
            episode = self.generate_episode()
            G = 0  # Initialize return
            for state, action, reward in reversed(episode):
                G = self.gamma * G + reward
                # First-visit Monte Carlo: only consider first occurrence of the state in the episode
                if state not in [x[0] for x in episode[:episode.index((state, action, reward))]]:
                    returns[state].append(G)

        # Update state values with the average return
        for state in self.states:
            if returns[state]:
                self.state_values[state] = np.mean(returns[state])

    def plot_state_values(self):
        values = np.zeros((self.height, self.width))
        for y in range(self.height):
            for x in range(self.width):
                values[y, x] = self.state_values[(x, y)]

        fig, ax = plt.subplots()
        ax.matshow(values, cmap='coolwarm')
        for i in range(self.height):
            for j in range(self.width):
                c = values[i, j]
                ax.text(j, i, f'{c:.2f}', va='center', ha='center')

        plt.colorbar(ax.matshow(values, cmap='coolwarm'), ax=ax)
        plt.title('Gridworld State Values')
        plt.show()

# Create an instance of the Gridworld with Monte Carlo implementation
gridworld_mc = GridworldMonteCarlo()

# Run the Monte Carlo evaluation
gridworld_mc.monte_carlo_evaluation(episodes=1000)

# Plot the resulting state values
gridworld_mc.plot_state_values()
