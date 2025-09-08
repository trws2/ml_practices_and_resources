import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    tmp = np.dot(np.transpose(X), X)
    tmp = np.linalg.inv(tmp)
    tmp = np.dot(tmp, np.transpose(X))
    theta = np.round(np.dot(tmp, y), 4).flatten().tolist()
    return theta

print(linear_regression_normal_equation([[1, 1], [1, 2], [1, 3]], [1, 2, 3]))


