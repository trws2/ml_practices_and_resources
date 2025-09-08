import numpy as np

def layer_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
	"""
	Perform Layer Normalization.
	"""
    m = np.mean(X, axis=(2), keepdims=True)
    s = np.std(X, axis=(2), keepdims=True)    
    val = (X - m) / s 
    return gamma * val + beta

