# https://www.deep-ml.com/problems/151

import numpy as np

class DropoutLayer:
    def __init__(self, p: float):
        """Initialize the dropout layer."""
        self.p = p
        self.mask = None

    def forward(self, x: np.ndarray, training: bool = True) -> np.ndarray:
        """Forward pass of the dropout layer."""
        if training:
            # the following is basically uniform distribution with prob=(1-self.p)
            # for sampled values being 1
            # it is more direct and efficient than the rand(...) code below
            self.mask = np.random.binomial(1, 1 - self.p, x.shape)
            # or using the following code is also a uniform distribution with 
            # values sampled from [0, 1)
            # self.mask = (np.random.rand(*x.shape) > self.p)
            return (x * self.mask) / (1 - self.p)
        else:
            return x

    def backward(self, grad: np.ndarray) -> np.ndarray:
        """Backward pass of the dropout layer."""
        if self.mask is None:
            raise ValueError("Forward pass must be called before backward pass")
        return grad * self.mask / (1 - self.p)

