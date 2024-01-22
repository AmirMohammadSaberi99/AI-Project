# AI-Project - Amirmohammad Saberi - S5840276

# Gridworld Monte Carlo

This project implements a Monte Carlo method for estimating state values in a Gridworld environment. The Gridworld is a simple 5x5 grid where each cell represents a state. The agent can move in four directions (North, South, East, West) with equal probability. The Monte Carlo method is used to estimate the value of each state based on the returns received by following this policy.

## Files

- `Amirmohammad Saberi- S5840276.py`: This Python script contains the implementation of the Gridworld environment and the Monte Carlo algorithm for policy evaluation.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Implementation Details

### Gridworld Environment

The `Gridworld` class represents the environment. It is a 5x5 grid with specific rewards set for some states. The agent can take actions to move in the grid, and the transition and reward dynamics are defined within this class.

### Monte Carlo Evaluation

The `GridworldMonteCarlo` class inherits from `Gridworld` and adds the functionality for Monte Carlo evaluation. It includes methods to generate episodes based on the current policy and to estimate state values using the first-visit Monte Carlo method.

### Visualization

The state values estimated by the Monte Carlo method is visualized using Matplotlib. In `Amirmohammad Saberi- S5840276` displays the values as numbers in each grid cell.

## Usage

Run the script `Amirmohammad Saberi- S5840276` to see the Monte Carlo evaluation in action and the resulting visualization of state values.

```
python Amirmohammad Saberi- S5840276.py


```

# Gridworld Monte Carlo Implementation

This repository contains a Python implementation of the Monte Carlo algorithm in a Gridworld environment. The `Gridworld` class encapsulates the environment and its dynamics.

## Environment Description

The Gridworld environment includes:

- A 5x5 grid of states.
- A policy with equal probabilities for moving North (N), South (S), East (E), and West (W) from each state.
- A discount factor (gamma) set to 0.9.
- Rewards assigned for specific states, with a default reward of 0 for most states. Special rewards are given to states (1, 0) and (3, 0).
- A `take_action` method for state transitions based on actions and returning the associated rewards.
- A `policy_evaluation` method for evaluating the current policy.

## Monte Carlo Algorithm Implementation

The implementation of the Monte Carlo algorithm in this environment involves the following steps:

1. Implementing a method for generating episodes based on the current policy.
2. Creating a Monte Carlo algorithm to estimate state values from the generated episodes.
3. Updating the state values based on the Monte Carlo estimation.

![gridworld](https://github.com/AmirMohammadSaberi99/AI-Project/assets/64252685/871802d5-ad60-4704-9337-ac8eda4135c6)

## State Value Results

After running the Monte Carlo algorithm for 1000 episodes, the state values are as follows:

```
  2.22   1.00   0.21  -0.39  -0.58
  9.69   3.04   0.89  -0.01  -0.40
  3.03   2.20   0.66   0.05  -0.43
  5.54   1.84   0.67  -0.01  -0.47
  0.77   0.49   0.07  -0.45  -0.75
```

These values indicate the estimated value of each state under the current policy, where the policy is to move in all four directions with equal probability from each state. Positive values signify more favorable states, while negative values indicate less favorable ones. The Monte Carlo method bases these estimates on the average return from multiple simulated episodes, reflecting the long-term benefits of being in each state under the given policy.




