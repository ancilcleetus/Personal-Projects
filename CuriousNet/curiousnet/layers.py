#!/usr/bin/env python3

"""
Our neural nets will be made up of layers.
Each layer needs to pass its inputs forward
and propagate gradients backward.
For example, a neural net might look like

inputs -> Linear -> Tanh -> Linear -> output
"""
import numpy as np

from curiousnet.tensor import Tensor

class Layer:
    def __init__(self) -> None:
        pass

    def forward(self, inputs: Tensor) -> Tensor:
        """
        Produce the outputs corresponding to these inputs
        """
        raise NotImplementedError
    
    def backward(self, grad: Tensor) -> Tensor:
        """
        Backpropagate this gradient through the layer
        """
        raise NotImplementedError
    