import numpy as np

def l1_regularization_gradient_descent(X: np.array, y: np.array, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    weights = weights.reshape(n_features, 1)
    bias = 0

    y = y.reshape(y.shape[0], 1)

    for i in range(max_iter):
        pred = np.dot(X, weights) + bias 
        error = pred - y

        grad_w = (1 / n_samples) * np.sum(error * X, axis=(0)).reshape(n_features, 1) + alpha * np.sign(weights)
        grad_b = sum(error) / n_samples

        weights -= learning_rate * grad_w
        bias -= learning_rate * grad_b

        if np.linalg.norm(grad_w, ord=1) < tol:
            break

    return weights, bias


X = np.array([[0, 0], [1, 1], [2, 2]])
y = np.array([0, 1, 2])

alpha = 0.1
weights, bias = l1_regularization_gradient_descent(X, y, alpha=alpha, learning_rate=0.01, max_iter=1000)

