import numpy as np
def swish(x: float) -> float:
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

	val = x * sigmoid(x)
	return round(val, 4)
