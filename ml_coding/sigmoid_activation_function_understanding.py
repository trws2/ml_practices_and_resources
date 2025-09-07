import math

def sigmoid(z: float) -> float:
	#Your code here
    result = 1 / (1 + math.exp(-z))
    # result = round(10000 * result) / 10000
	return round(result, 4)
