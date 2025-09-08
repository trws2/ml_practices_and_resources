import numpy as np
from numpy.random import randn

N, D_in, H, D_out = 64, 1000, 100, 10
X, Y = randn(N, D_in), randn(N, D_out)
W1, W2 = randn(D_in, H), randn(H, D_out)
lr = 1e-4

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def compute_MSE_loss(error):
    mse = np.mean(np.sum(error**2, axis=1))
    return mse

for t in range(100000):
    # forward pass
    H = sigmoid(np.dot(X, W1))
    Y_pred = np.dot(H, W2)
    
    error = Y_pred - Y
    # compute and print loss
    loss = compute_MSE_loss(error)
    if t % 100 == 0:
        print(f"iter={t}, loss = {loss}")

    # backward pass
    dW2 = np.dot(H.T, 2*error)
    dW1 = np.dot(X.T, np.dot(2*error, W2.T) * H * (1 - H))

    # update weights
    W1 -= lr * dW1
    W2 -= lr * dW2
