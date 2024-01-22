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



