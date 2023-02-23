#!/usr/bin/env python3

"""
We use an optimizer to adjust the parameters
of our network based on the gradients computed
during backpropagation
"""
from curiousnet.nn import NeuralNet

class Optimizer:
    def step(self, net: NeuralNet) -> None:
        raise NotImplementedError
