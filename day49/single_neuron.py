import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
    f = lambda x : sum([w_i * x_i for w_i, x_i in zip(weights, x)]) + bias
    logits = [f(x) for x in features]
    f = lambda x : 1 / (1 + math.exp(-x))
    probabilities = [f(x) for x in logits]
    mse = [(p - l) ** 2 for p, l in zip(probabilities, labels)]
    mse = sum(mse) / len(mse)
    mse = round(mse, 4)
    probabilities = [round(p, 4) for p in probabilities]
	return probabilities, mse
