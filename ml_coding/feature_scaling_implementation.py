import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here

    m = np.mean(data, axis=(0), keepdims=True)
    s = np.sqrt(np.var(data, axis=(0), keepdims=True))
    minimum = np.min(data, axis=(0), keepdims=True)
    maximum = np.max(data, axis=(0), keepdims=True)

    standardized_data = (data - m) / s
    normalized_data = (data - minimum) / (maximum - minimum)

	return standardized_data, normalized_data
