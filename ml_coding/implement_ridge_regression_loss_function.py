import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    a = np.dot(X, w) - y_true
    a = np.mean(a**2)
    a = a + alpha * sum(w**2)
    return a

