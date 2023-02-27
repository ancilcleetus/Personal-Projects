#!/usr/bin/env python3

"""
FizzBuzz is the following problem:
For each of the numbers 1 to 100:
    * if the number is divisible by 3, print "fizz"
    * if the number is divisible by 5, print "buzz"
    * if the number is divisible by 15, print "fizzbuzz"
    * otherwise, just print the number

This can be modeled as a four-class classificatiion problem
(fizz, buzz, fizzbuzz, number) which can be solved with a neural net
"""

from typing import List

import numpy as np

from curiousnet.train import train
from curiousnet.nn import NeuralNet
from curiousnet.layers import Linear, Tanh
from curiousnet.optim import SGD

def fizz_buzz_encode(x: int) -> List[int]:
    if x % 15 == 0:
        return [0, 0, 0, 1]
    elif x % 5 == 0:
        return [0, 0, 1, 0]
    elif x % 3 == 0:
        return [0, 1, 0, 0]
    else:
        return [1, 0, 0, 0]


def binary_encode(x: int) -> List[int]:
    """
    10 digit binary encoding of x
    """
    return [x >> i & 1 for i in range(0, 10)]

# Since we want to predict for inputs 1 to 100,
# we train the neural net with inputs from 101 to 1024
inputs = np.array([
    binary_encode(x)
    for x in range(101, 1024)
])

targets = np.array([
    fizz_buzz_encode(x)
    for x in range(101, 1024)
])

net = NeuralNet([
    Linear(input_size=10, output_size=50),
    Tanh(),
    Linear(input_size=50, output_size=4)
])

train(net, inputs, targets, num_epochs=5000, optimizer=SGD(lr=0.001))

for x in range(1, 101):
    predicted = net.forward(binary_encode(x))
    predicted_idx = np.argmax(predicted)
    actual_idx = np.argmax(fizz_buzz_encode(x))
    labels = [str(x), "fizz", "buzz", "fizzbuzz"]
    print(f"input = {x}\tpredicted_output = {labels[predicted_idx]}\tactual_output = {labels[actual_idx]}")
