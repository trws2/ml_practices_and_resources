def min_max(x: list[int]) -> list[float]:
	min_val = min(x)
	max_val = max(x)
	diff = max_val - min_val

	if diff == 0:
		return [0.0] * len(x)

	return [(e - min_val) / diff for e in x]

