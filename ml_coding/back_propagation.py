
import numpy as np

class NeutralNetwork:
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        np.random.seed(42)
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.W1 = np.random.randn(input_size, hidden_size) * (1 / np.sqrt(input_size))
        self.W2 = np.random.randn(hidden_size, output_size) * (1 / np.sqrt(hidden_size))
        self.act_type = "relu"
        self.loss_type = "bce"

    def sigmoid(self, z: np.ndarray) -> np.ndarray:
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, A: np.ndarray) -> np.ndarray:
        return A * (1 - A)

    def relu(self, z: np.ndarray) -> np.ndarray:
        return np.maximum(0, z)

    def relu_derivative(self, A: np.ndarray) -> np.ndarray:
        return (A > 0).astype(float)

    def forward(self, X: np.ndarray) -> np.ndarray:
        self.Z1 = np.matmul(X, self.W1)
        if self.act_type == "relu":
            self.A1 = self.relu(self.Z1)
        else:
            self.A1 = self.sigmoid(self.Z1)
        self.Z2 = np.matmul(self.A1, self.W2)
        self.A2 = self.sigmoid(self.Z2)
        return self.A2

    def compute_loss(self, prob: np.ndarray, y: np.ndarray) -> float:
        if self.loss_type == "bce":
            eps = 1e-12
            prob_clip = np.clip(prob, eps, 1 - eps)
            return -np.mean(y * np.log(prob_clip) + (1 - y) * np.log(1 - prob_clip))
        else:
            return np.mean((prob - y) ** 2)

    def backward(self, X: np.ndarray, prob: np.ndarray, y: np.ndarray, learning_rate: float) -> None:
        # propagate error
        if self.loss_type == "bce":
            W2_delta = prob - y
        else:
            output_error = prob - y
            W2_delta = output_error * self.sigmoid_derivative(self.A2)

        if self.act_type == "relu":
            W1_delta = np.matmul(W2_delta, self.W2.T) * self.relu_derivative(self.A1) 
        else:
            W1_delta = np.matmul(W2_delta, self.W2.T) * self.sigmoid_derivative(self.A1) 

        # compute gradient
        m = X.shape[0]
        W2_grad = np.matmul(self.A1.T, W2_delta) / m
        W1_grad = np.matmul(X.T, W1_delta) / m

        # update weights
        self.W2 -= learning_rate * W2_grad
        self.W1 -= learning_rate * W1_grad

    def train(self, X: np.ndarray, y: np.ndarray, learning_rate: float, max_iters: int, eps: float):
        all_losses = []
        break_from_loop = False
        for i in range(max_iters):
            prob = self.forward(X)
            loss = self.compute_loss(prob, y)
            all_losses.append(loss)
            if i % 100 == 0:
                print(f"iter={i}, loss={loss}")
            if i > 0:
                diff = abs(all_losses[-1] - all_losses[-2]) / (abs(all_losses[-2]) + 1e-12)
                if diff < eps:
                    print(f"Finished: iter={i}, loss={loss}, diff={diff}")
                    break_from_loop = True
                    break
            self.backward(X, prob, y, learning_rate)

        if not break_from_loop:
            print(f"Finished: max iteration reached, loss={all_losses[-1]}, diff={diff}")
        

if __name__ == "__main__":
    # XOR datase; adding bias term value (1) in the end of each examples
    X = np.array([[0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]])
    y = np.array([[0], [1], [1], [0]])

    net = NeutralNetwork(3, 10, 1)

    max_iters = 100000
    learning_rate = 0.1
    eps = 1e-8
    net.train(X, y, learning_rate, max_iters, eps)

    prob = net.forward(X)
    pred = prob >= 0.5
    print(f"prob = {prob}")
    print(f"pred = {pred}")

