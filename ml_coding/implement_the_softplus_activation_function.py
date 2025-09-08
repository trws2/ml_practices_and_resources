import numpy as np
def softplus(x: float) -> float:
	# Your code here
	val = np.log(1 + np.exp(x))
	return round(val,4)
