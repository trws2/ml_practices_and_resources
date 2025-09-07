def hard_sigmoid(x: float) -> float:
	# Your code here
	return max(0.0, min(1.0, (2.0*x+5)/10))
