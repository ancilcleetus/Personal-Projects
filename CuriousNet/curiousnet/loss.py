#!/usr/bin/env python3

"""
A Loss Function measures how good our predictions are.
We can use it to adjust the parameters of our neural net.
"""

import numpy as np

from curiousnet.tensor import Tensor

class Loss:
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        raise NotImplementedError
    
    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        raise NotImplementedError
    

class MSE(Loss):
    """
    MSE -> Mean Squared Error
    We're actually implementing Total Squared Error instead of MSE
    """
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        return np.sum((predicted - actual) ** 2)
    
    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        return 2 * (predicted - actual)
