import torch
import torch.nn as nn
import torch.nn.functional as F

class PolicyNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size) #input layer
        self.fc2 = nn.Linear(hidden_size, output_size) #hidden layer

    def forward(self, x):
        x = F.relu(self.fc1(x)) #activation function chosen relu
        #x = F.relu(self.fc2(x))
        x = self.fc2(x)
        return x