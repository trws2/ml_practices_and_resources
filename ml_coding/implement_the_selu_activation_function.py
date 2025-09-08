import numpy as np
def selu(x: float) -> float:
	alpha = 1.6732632423543772
	scale = 1.0507009873554804
	
    val = scale * x if x > 0 else alpha * scale * (np.exp(x) - 1)
	return round(val, 4)
