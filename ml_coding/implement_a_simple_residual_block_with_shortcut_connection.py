import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
    tmp = np.dot(w1, x)
    tmp = np.dot(w2, tmp)
    tmp = np.maximum(0, tmp) + x
    val = np.maximum(0, tmp)
    return np.round(val, 4)

