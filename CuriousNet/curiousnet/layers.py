#!/usr/bin/env python3

"""
Our neural nets will be made up of layers.
Each layer needs to pass its inputs forward
and propagate gradients backward.
For example, a neural net might look like

inputs -> Linear -> Tanh -> Linear -> output
"""
from typing import Dict

import numpy as np

from curiousnet.tensor import Tensor

class Layer:
    def __init__(self) -> None:
        self.params: Dict[str, Tensor] = {}
        self.grads: Dict[str, Tensor] = {}

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


class Linear(Layer):
    """
    Computes output = inputs @ w + b
    """
    def __init__(self, input_size: int, output_size: int) -> None:
        super().__init__()
        # inputs will be of shape (batch_size, input_size)
        # outputs will be of shape (batch_size, output_size)
        self.params["w"] = np.random.randn(input_size, output_size)
        self.params["b"] = np.random.randn(output_size)

    def forward(self, inputs: Tensor) -> Tensor:
        """
        output = inputs @ w + b
        """
        self.inputs = inputs
        return inputs @ self.params["w"] + self.params["b"]
    
    def backward(self, grad: Tensor) -> Tensor:
        """
        If y = f(x) and x = a * b + c, then
        dy/da = f'(x) * b
        dy/db = f'(x) * a
        dy/dc = f'(x)

        If y = f(x) and x = a @ b + c, then
        dy/da = f'(x) @ b.T
        dy/db = a.T @ f'(x)
        dy/dc = f'(x)
        """
        self.grads["b"] = np.sum(grad, axis=0)
        self.grads["w"] = self.inputs.T @ grad
        return grad @ self.params["w"].T