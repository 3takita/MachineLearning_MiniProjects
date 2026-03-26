# Reinforcement Learning Example: Q-Learning
# -----------------------------------------
# Scenario:
# A delivery robot learns how to reach a goal location
# by moving LEFT or RIGHT along a 1D path.

import numpy as np
import random

# -----------------------------
# Step 1: Environment Settings
# -----------------------------
num_states = 5          # positions: 0 → 4
goal_state = 4         # goal position
num_actions = 2        # 0 = LEFT, 1 = RIGHT

# -----------------------------
# Step 2: Initialize Q-table
# -----------------------------
# Rows = states, Columns = actions
Q = np.zeros((num_states, num_actions))

# -----------------------------
# Step 3: Hyperparameters
# -----------------------------
learning_rate = 0.1    # how quickly the model updates knowledge
gamma = 0.9            # discount factor (future rewards importance)
epsilon = 0.3          # exploration probability
episodes = 100         # number of training runs

# -----------------------------
# Step 4: Environment Function
# -----------------------------
def step(state, action):
    """
    Simulates taking an action from a given state.

    Parameters:
        state (int): current position
        action (int): 0 (LEFT) or 1 (RIGHT)

    Returns:
        next_state (int): new position after action
        reward (int): reward received (1 if goal reached)
    """

    # Move LEFT
    if action == 0:
        next_state = max(state - 1, 0)
    # Move RIGHT
    else:
        next_state = min(state + 1, goal_state)

    # Reward only when goal is reached
    reward = 1 if next_state == goal_state else 0

    return next_state, reward

# -----------------------------
# Step 5: Training Loop
# -----------------------------
for episode in range(episodes):
    state = 0  # start from position 0

    while state != goal_state:

        # Epsilon-greedy strategy:
        # Explore (random action) or Exploit (best known action)
        if random.random() < epsilon:
            action = random.choice([0, 1])
        else:
            action = np.argmax(Q[state])

        # Take action
        next_state, reward = step(state, action)

        # Q-learning formula
        old_value = Q[state, action]
        best_future_value = np.max(Q[next_state])

        Q[state, action] = old_value + learning_rate * (
            reward + gamma * best_future_value - old_value
        )

        # Move to next state
        state = next_state

# -----------------------------
# Step 6: Results
# -----------------------------
print("Learned Q-table:\n")
print(Q)

print("\nBest action at each state:")
for state in range(num_states):
    best_action = np.argmax(Q[state])
    action_name = "LEFT" if best_action == 0 else "RIGHT"
    print(f"State {state}: {action_name}")
