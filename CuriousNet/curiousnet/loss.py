#!/usr/bin/env python3

"""
A Loss Function measures how good our predictions are.
We can use it to adjust the parameters of our neural net.
"""

import numpy as np

from curiousnet.tensor import Tensor

class Loss:
    """
    A base class for defining loss functions and their gradients.

    Attributes:
    -----------
    None

    Methods:
    --------
    loss(predicted: Tensor, actual: Tensor) -> float:
        Computes the loss given the predicted and actual outputs.

    grad(predicted: Tensor, actual: Tensor) -> Tensor:
        Computes the gradient of the loss with respect to the predicted output.

    """
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        """
        Computes the loss given the predicted and actual outputs.

        Parameters:
        -----------
        predicted: Tensor
            The predicted output of the model.
        actual: Tensor
            The actual output of the model.

        Returns:
        --------
        float
            The loss value computed using the predicted and actual outputs.
        """
        raise NotImplementedError("Subclass must implement abstract method")
    
    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        """
        Computes the gradient of the loss with respect to the predicted output.

        Parameters:
        -----------
        predicted: Tensor
            The predicted output of the model.
        actual: Tensor
            The actual output of the model.

        Returns:
        --------
        Tensor
            The gradient of the loss with respect to the predicted output.
        """
        raise NotImplementedError("Subclass must implement abstract method")
    

class MSE(Loss):
    """
    MSE -> Mean Squared Error
    We're actually implementing Total Squared Error instead of MSE
    """
    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        """
        Computes the Mean Squared Error (MSE) given the predicted and actual outputs.

        Parameters:
        -----------
        predicted: Tensor
            The predicted output of the model.
        actual: Tensor
            The actual output of the model.

        Returns:
        --------
        float
            The MSE value computed using the predicted and actual outputs.
        """
        return np.sum((predicted - actual) ** 2)
    
    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        """
        Computes the gradient of the Mean Squared Error (MSE) with respect to the predicted output.

        Parameters:
        -----------
        predicted: Tensor
            The predicted output of the model.
        actual: Tensor
            The actual output of the model.

        Returns:
        --------
        Tensor
            The gradient of the MSE with respect to the predicted output.
        """
        return 2 * (predicted - actual)
