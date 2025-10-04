# source: https://www.deep-ml.com/problems/106

import numpy as np

def train_logreg(X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int) -> tuple[list[float], ...]:
    # add bias value to X
    one_col = np.ones((X.shape[0],1))
    X = np.append(X, one_col, axis=-1)

    weights = np.random.rand(X.shape[1])
    # weights = np.zeros(X.shape[1])
    all_losses = []

    def sigmoid(z):
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    def compute_prob(weights, X):
        return sigmoid(np.matmul(X, weights))

    def compute_loss(y, p):
        return -np.sum(y * np.log(p) + (1 - y) * np.log(1 - p))

    def compute_gradient(y, p, X):
        diff = (y - p).reshape((y.shape[0], 1))
        return -np.mean(diff * X, axis=0)

    for i in range(iterations):
        # compute prob
        prob = compute_prob(weights, X)

        # compute loss
        loss = compute_loss(y, prob)
        all_losses.append(loss)

        # if loss converage, break
        if i > 0:
            loss_change = abs(all_losses[-1] - all_losses[-2]) / all_losses[-2]
            if loss_change < 1e-6:
                break

        # compute gradient
        grad = compute_gradient(y, prob, X)

        # update weights by moving 1 step along gradient direction
        weights = weights - learning_rate * grad
        
    return weights, all_losses


print(train_logreg(np.array([[0.7674, -0.2341, -0.2341, 1.5792], [-1.4123, 0.3142, -1.0128, -0.9080], [-0.4657, 0.5425, -0.4694, -0.4634], [-0.5622, -1.9132, 0.2419, -1.7249], [-1.4247, -0.2257, 1.4656, 0.0675], [1.8522, -0.2916, -0.6006, -0.6017], [0.3756, 0.1109, -0.5443, -1.1509], [0.1968, -1.9596, 0.2088, -1.3281], [1.5230, -0.1382, 0.4967, 0.6476], [-1.2208, -1.0577, -0.0134, 0.8225]]), np.array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0]), 0.001, 10))
