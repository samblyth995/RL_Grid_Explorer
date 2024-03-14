import csv
import torch
import torch.optim as optim
import numpy as np
from Agent_Policy import PolicyNetwork
from Grid_game import GridEnvironment
import torch.nn.functional as F

# Parameters
NUM_EPISODES = 1000
MAX_STEPS_PER_EPISODE = 20
BATCH_SIZE = 64
GAMMA = 0.99
EPSILON_START = 1.0
EPSILON_END = 0.01
EPSILON_DECAY = 0.995
#EPSILON_DECAY = np.random.uniform(0.1, 0.9)
TARGET_UPDATE_FREQ = 10
MEMORY_SIZE = 10000

# Initialize environment
env = GridEnvironment()
state_size = 2  # Assuming the state representation is the agent's (x, y) position
action_size = 4  # Up, Right, Down, Left
hidden_size = 64

# Initialize Q-network and target network
q_network = PolicyNetwork(input_size=state_size, hidden_size=hidden_size, output_size=action_size)
target_network = PolicyNetwork(input_size=state_size, hidden_size=hidden_size, output_size=action_size)
target_network.load_state_dict(q_network.state_dict())  # Initialize target network with the same weights as Q-network
target_network.eval()  # Set target network to evaluation mode (no gradients)

# Initialize optimizer
optimizer = optim.Adam(q_network.parameters(), lr=0.01)

# Experience replay buffer
memory = []

# Function to select an action using epsilon-greedy strategy
def select_action(state, epsilon):
    if np.random.rand() < epsilon:
        return np.random.choice(action_size)  # Random action
    else:
        with torch.no_grad():
            q_values = q_network(torch.FloatTensor(state))
            return q_values.argmax().item()  # Greedy action

##write runs to csv
with open('training_runs_optim_POLICY_6_X_6.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Define your headers based on what you want to track. For example:
    headers = ['Episode', 'Total Reward', 'Steps Taken', 'state', 'Path', 'Final_position','Epsilon', 'Done']
    writer.writerow(headers)

# Main training loop
epsilon = EPSILON_START
for episode in range(NUM_EPISODES):
    path=[]
    #state = [0, 0]  # Reset environment
    state = env.reset()
    print(f"new episode reset postion is {env.agent_position}")
    total_reward = 0
    done=False
    
    for step in range(MAX_STEPS_PER_EPISODE):
        if done:
            break
        action = select_action(state, epsilon)
        env.move_agent(action)
        next_state = env.agent_position
        
        reward, done = env.get_reward()  # Get reward
        total_reward += reward
    
        memory.append((state, action, reward, next_state))
        state = next_state
        path.append(state)
    
    

        # Sample a mini-batch from memory and update Q-network
        if len(memory) >= BATCH_SIZE:
            batch = np.random.choice(len(memory), BATCH_SIZE, replace=False)
            state_batch, action_batch, reward_batch, next_state_batch = zip(*[memory[i] for i in batch])
            state_batch = torch.FloatTensor(state_batch)
            action_batch = torch.LongTensor(action_batch)
            reward_batch = torch.FloatTensor(reward_batch)
            next_state_batch = torch.FloatTensor(next_state_batch)

            # Calculate target Q-values using target network
            with torch.no_grad():
                target_q_values = reward_batch + GAMMA * target_network(next_state_batch).max(dim=1)[0]

            # Calculate predicted Q-values using Q-network
            q_values = q_network(state_batch)
            predicted_q_values = q_values.gather(dim=1, index=action_batch.unsqueeze(dim=1)).squeeze(dim=1)

            # Compute Huber loss
            loss = F.smooth_l1_loss(predicted_q_values, target_q_values)

            # Optimize the model
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        state = next_state

    # Update epsilon
    epsilon = max(EPSILON_END, EPSILON_DECAY * epsilon)

    # Update target network
    if episode % TARGET_UPDATE_FREQ == 0:
        target_network.load_state_dict(q_network.state_dict())
    final_position= env.agent_position

    action = select_action(state, epsilon)
    print(f"Selected action: {action}")
    env.move_agent(action)  # Ensure this is the correct method name
    print(path)

    print(f"Episode {episode + 1}, Total Reward: {total_reward}, Final position {final_position}, done = {done}")
    # if done:
    #     break
# print info to csv
    with open('training_runs_optim_POLICY_6_X_6.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        final_position= env.agent_position
        path_str=';'.join(map(str,path))
        # Create a list of the data you want to record. For example:
        data = [episode + 1, total_reward, step+1, state, path_str, final_position, epsilon, done]
        writer.writerow(data)


print("Training finished.")
