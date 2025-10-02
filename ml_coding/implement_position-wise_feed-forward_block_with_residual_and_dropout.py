# https://www.deep-ml.com/problems/178

import numpy as np

def ffn(x: list[float], W1: list[list[float]], b1: list[float], W2: list[list[float]], b2: list[float], dropout_p: float=0.1, seed: int=42) -> list[float]:
	"""
	Implement a position-wise feed-forward block with residual and dropout.

	Args:
		x: input vector
		W1, b1: first linear layer parameters
		W2, b2: second linear layer parameters
		dropout_p: dropout probability
		seed: random seed for reproducibility

	Returns:
		Output vector after FFN block (rounded to 4 decimals)
	"""
    # this can only happen during training's forward pass, not during inference
    def dropout(X):
        # randomly drop dropout_p samples
        mask = (np.random.rand(*X.shape) > dropout_p).astype(float)
        X = X * mask
        # scale the rest of samples by 1 / (1 - dropout_p)
        X = X / (1 - dropout_p)
        return X

    np.random.seed(seed)
    X = np.array(x)
    W1 = np.array(W1)
    W2 = np.array(W2)        

    Z1 = np.dot(W1, X) + b1
    A1 = np.maximum(0, Z1)

    Z2 = np.dot(W2, A1) + b2
    residual = Z2 + X
    output = dropout(residual)

    return [round(v,4) for v in output.tolist()]


