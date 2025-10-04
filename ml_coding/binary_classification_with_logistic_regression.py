# source: https://www.deep-ml.com/problems/104
import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
    def sigmoid(z: np.ndarray) -> np.ndarray:
        # prevent overflow
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))
    z = np.matmul(X, weights) + bias
    s = sigmoid(z)
    pred = (s >= 0.5).astype(int)
    return pred

print(predict_logistic(np.array([[0, 0], [0.1, 0.1], [-0.1, -0.1]]), np.array([1, 1]), 0))

