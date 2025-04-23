import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
    def f(score, sub):
    	return score - sub
    sub = np.log(sum(np.exp(scores)))
    ret = [round(f(s, sub), 4) for s in scores]
    return ret

