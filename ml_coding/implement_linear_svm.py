
import numpy as np
from sklearn.datasets import make_classification
from sklearn.datasets import train_test_split


def make_classification_dataset():
    X, y = make_classification(n_features=5, n_samples=100, n_informative=5, n_redundant=0, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

class SVM:
    def __init__(self, C: float, num_features: int):
        self.C = C
        self.weights = np.random.uniform(low=0, high=1, size=(num_features,))
        self.bias = np.random.rand()

    def train(self, X_train: np.ndarray, y_train: np.ndarray, learning_rate: float):
        pass

    def predict(X_test: np.ndarray) -> np.ndarray:
        tmp = np.matmul(X_train, self.weights) + self.bias
        return np.sign(tmp)

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = make_classification_dataset()
    print(f"number of training data {train_y.shape[0]}")
    print(f"number of testing data {train_y.shape[0]}")

    C = 1.0
    learning_rate = 0.01
    svm = SVM(C)
    svm.train(X_train, y_train, learning_rate)
    pred = svm.predict(X_test)

    num_test_examples = y_test.shape[0]
    accuracy = np.sum(y_test == pred) / num_test_examples
    print(f"prediction accuracy on testing data is {accuracy}")
