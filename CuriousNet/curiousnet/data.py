#!/usr/bin/env python3

"""
We will feed inputs into our network in batches.
So here are some tools for iterating over data in batches.
"""
from typing import Iterator, NamedTuple

import numpy as np

from curiousnet.tensor import Tensor

Batch = NamedTuple("Batch", [("inputs", Tensor), ("targets", Tensor)])

class DataIterator:
    def __call__(self, inputs: Tensor, targets: Tensor) -> Iterator[Batch]:
        raise NotImplementedError
    