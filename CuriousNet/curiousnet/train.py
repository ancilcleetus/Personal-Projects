#!/usr/bin/env python3

"""
A function that can train a Neural Net
"""
from curiousnet.tensor import Tensor
from curiousnet.nn import NeuralNet
from curiousnet.loss import Loss, MSE
from curiousnet.optim import Optimizer, SGD
from curiousnet.data import DataIterator, BatchIterator


def train(
        net: NeuralNet, 
        inputs: Tensor, 
        targets: Tensor, 
        num_epochs: int = 5000, 
        iterator: DataIterator = BatchIterator(), 
        loss: Loss = MSE(), 
        optimizer: Optimizer = SGD()
    ) -> None:
    for epoch in range(0, num_epochs):
        epoch_loss = 0.0
        for batch in iterator(inputs, targets):
            predicted = net.forward(batch.inputs)
            epoch_loss += loss.loss(predicted, batch.targets)
            grad = loss.grad(predicted, batch.targets)
            net.backward(grad)
            optimizer.step(net)
        print(f"epoch = {epoch}, epoch_loss = {epoch_loss}")
