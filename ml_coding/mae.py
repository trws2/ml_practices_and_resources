import numpy as np

def mae(y_true, y_pred):
	val = np.mean(np.abs(y_true - y_pred))
	return round(val,3)
