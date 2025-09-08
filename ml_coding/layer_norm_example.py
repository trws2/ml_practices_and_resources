import numpy as np


# token embedding for "cat" in "the cat sat"
x = [0.8, -1.2, 2.5, 0.3]
x = np.array(x)

m = np.mean(x)
var = np.var(x)
std = np.sqrt(var)

x_normalized = (x - m) / std

gamma = np.array([1.1, 0.9, 1.2, 1.0])
beta = np.array([0.1, 0, -0.1, 0.2])

x_normalized_scaled_shifted = gamma * x_normalized + beta

print(f"x_normalized_scaled_shifted={x_normalized_scaled_shifted}")

