import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
    def predict(features, weights, bias):
        z = np.dot(features, weights) + bias
        return 1 / (1 + np.exp(-z))
    
    def grad(errors, features, labels, predictions):
        weight_gradients = (2/len(labels)) * np.dot(features.T, errors * predictions * (1 - predictions))
        bias_gradient = (2/len(labels)) * np.sum(errors * predictions * (1 - predictions))
        return weight_gradients, bias_gradient

    weights = np.array(initial_weights)
    bias = initial_bias
    labels = np.array(labels)
    mse_values = []

    for _ in range(epochs):
        predictions = predict(features, weights, bias)
        errors = predictions - labels
        mse = np.mean(errors ** 2)
        mse_values.append(round(mse, 4))

        weight_gradients, bias_gradient = grad(errors, features, labels, predictions)
        
        weights -= learning_rate * weight_gradients
        bias -= learning_rate * bias_gradient

        updated_weights = np.round(weights, 4)
        updated_bias = round(bias, 4)

    return updated_weights.tolist(), updated_bias, mse_values

