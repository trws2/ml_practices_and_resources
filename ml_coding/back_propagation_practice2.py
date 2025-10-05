# 1. code a 2-layer neutral network to classify XOR data dataset
# 2. user RELU as activation function in the hidden layer
# 3. user binary cross entropy loss to compute the loss
# 
# import numpy as np
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# y = np.array([[0], [1], [1], [0]])


import numpy as np

class NeutralNetwork:
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.W1 = np.random.randn(input_size, hidden_size) / np.sqrt(input_size)
        self.W2 = np.random.randn(hidden_size, output_size) / np.sqrt(hidden_size)        

    def relu(self, Z: np.ndarray) -> np.ndarray:
        return np.maximum(0, Z)

    def relu_derivertive(self, Z: np.ndarray) -> np.ndarray:
        return (Z > 0).astype(float)

    def sigmoid(self, Z: np.ndarray) -> np.ndarray:
        tmp = np.clip(Z, -500, 500)
        return 1 / (1 + np.exp(-tmp))

    def forward(self, X: np.ndarray) -> np.ndarray:
        self.Z1 = np.matmul(X, self.W1)
        self.A1 = self.relu(self.Z1)

        self.Z2 = np.matmul(self.A1, self.W2)
        self.A2 = self.sigmoid(self.Z2)

        return self.A2

    def compute_loss(self, prob: np.ndarray, y: np.ndarray):
        prob_clip = np.clip(prob, eps, 1 - eps)
        return -np.mean(y * np.log(prob_clip) + (1 - y) * np.log(1 - prob_clip))

    def backward(self, X: np.ndarray, prob: np.ndarray, y: np.ndarray, learning_rate: float) -> None:
        # W1_delta
        W2_delta = prob - y

        # W2_delta
        W1_delta = np.matmul(W2_delta, self.W2.T) * self.relu_derivertive(self.Z1)

        # W2_grad
        W2_grad = np.matmul(self.A1.T, W2_delta)

        # W1_grad
        W1_grad = np.matmul(X.T, W1_delta)

        # update W2
        self.W2 -= learning_rate * W2_grad

        # update W1
        self.W1 -= learning_rate * W1_grad

    def train(self, X: np.ndarray, y: np.ndarray, max_iters: int, learning_rate: float, eps: float) -> None:
        all_losses = []
        for i in range(max_iters):
            # run a forward pass
            prob = self.forward(X)

            # compute loss
            loss = self.compute_loss(prob, y)

            # check for convergence
            all_losses.append(loss)
            if i % 1000:
                print(f"iter={i}, loss={all_losses[-1]}")
            if i > 0:
                if abs(all_losses[-1] - all_losses[-2]) / (all_losses[-2] + 1e-12) < eps:
                    print(f"converged at iter={i}, loss={all_losses[-1]}")
                    break

            # if not converge, do a backward pass
            self.backward(X, prob, y, learning_rate)


if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    
    # add bias value to X
    bias_value = np.array([[1], [1], [1], [1]])
    X_add_bias_value = np.append(X, bias_value, axis=-1)

    # create NN class
    net = NeutralNetwork(3, 10, 1)

    # do training
    max_iters = 100000
    learning_rate = 0.1
    eps = 1e-7
    net.train(X_add_bias_value, y, max_iters, learning_rate, eps)

    # do prediction    
    prob = net.forward(X_add_bias_value)

    # print results
    print(f"prob={prob}")
    print(f"pred={prob >= 0.5}")

