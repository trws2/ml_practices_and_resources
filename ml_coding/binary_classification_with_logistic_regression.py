

import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
    y = np.dot(X, weights) + bias
    prob = 1 / (1 + np.exp(-y))
    pred = prob >= 0.5
    pred = pred.astype(int)
    pred = pred.tolist()
    return pred


print(predict_logistic(np.array([[0, 0], [0.1, 0.1], [-0.1, -0.1]]), np.array([1, 1]), 0))

