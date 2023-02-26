#!/usr/bin/env python3

"""
The canonical example of a function that can't be
learned with a simple linear model is XOR
"""
import numpy as np

from curiousnet.train import train
from curiousnet.nn import NeuralNet
from curiousnet.layers import Linear, Tanh

inputs = np.array([
    [0, 0], 
    [0, 1], 
    [1, 0], 
    [1, 1]
])

targets = np.array([
    [1, 0], 
    [0, 1], 
    [0, 1], 
    [1, 0]
])

net = NeuralNet([
    Linear(input_size=2, output_size=2), 
    Tanh(), 
    Linear(input_size=2, output_size=2)
])

train(net, inputs, targets)

for x, y in zip(inputs, targets):
    predicted = net.forward(x)
    print(f"x = {x}, predicted = {predicted}, y = {y}")