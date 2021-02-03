
import torch.nn as nn
import torch.nn.functional as F

class ReLu_Model(nn.Module):
    def __init__(self):
        super(ReLu_Model, self).__init__()

    def forward(self, x):
        return F.relu(x)

