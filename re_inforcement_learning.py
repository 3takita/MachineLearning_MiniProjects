# Reinforcement Learning - learning from consequences
# Delivery Robot Learning to Reach Destination

# Implementing: State, action, step(), reward, Q-table, episodes (practice attempts)

import numpy as np
import random

# Step 1: environment settings
num_states = 5
num_actions = 2
goal_state = 4

# Step 2: create the Q-table
Q = np.zeros((num_states, num_actions))

# Step 3: setting learning parameters
learning_rate = 0.1
gamma = 0.9  # importance of future rewards
epsilon = 0.3  # probability of random exploration
episodes = 100  # number of training rounds

# Step 4: define the environment transition
def step(state, action):
    if action == 0: 
        next_state = max(state - 1, 0)
    else:
        next_state = min(state + 1, goal_state)

    reward = 1 if next_state == goal_state else 0
    return next_state, reward

# Step 5: train robot using Q-learning
for episode in range(episodes):
    state = 0

    while state != goal_state:
        # epsilon-greedy strategy
        if random.random() < epsilon:
            action = random.choice([0, 1])
        else:
            action = np.argmax(Q[state])
        
        next_state, reward = step(state, action)

        old_value = Q[state, action]
        best_future_value = np.max(Q[next_state])

        # Q-learning update
        Q[state, action] = old_value + learning_rate * (
            reward + gamma * best_future_value - old_value
        )

        state = next_state

print("Learned Q-table:\n")
print(Q)

print("\nBest action at each state:")
for state in range(num_states):
    best_action = np.argmax(Q[state])

    action_name = "LEFT" if best_action == 0 else "RIGHT"
    print(f"State {state}: best action = {action_name}")

print("\nRobot following the learned policy:")

state = 0
path = [state]

while state != goal_state:
    action = np.argmax(Q[state])
    next_state, reward = step(state, action)
    path.append(next_state)
    state = next_state0

print("Path taken by robot:", path)

