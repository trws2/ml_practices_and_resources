import numpy as np

def layer_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
	"""
	Perform Layer Normalization.
	"""
    m = np.mean(X, axis=-1, keepdims=True)
    v = np.var(X, axis=-1, keepdims=True)
    val = (X - m) / np.sqrt(v + 1e-6)
    return gamma * val + beta


def batch_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
	"""
	Perform Layer Normalization.
	"""
    m = np.mean(X, axis=(1, 2), keepdims=True)
    v = np.var(X, axis=(1, 2), keepdims=True)
    val = (X - m) / np.sqrt(v + 1e-6)
    return gamma * val + beta


