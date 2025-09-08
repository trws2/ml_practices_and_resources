def softsign(x: float) -> float:
    # offter an alternative to tanh activation function
	# Your code here
	val = x / (1 + abs(x))
	return round(val,4)
