import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
    f = lambda x : math.exp(x)
    l = [f(x) for x in scores]
    sum_l = sum(l)
    f = lambda x : round(x / sum_l, 4)
    probabilities = [f(x) for x in l]
	return probabilities
