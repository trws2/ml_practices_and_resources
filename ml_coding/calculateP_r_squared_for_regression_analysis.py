import numpy as np

def r_squared(y_true, y_pred):
    m = np.mean(y_pred)
    TSS = sum((y_pred - m)**2)
    if TSS == 0:
        return 0.0

    RSS = sum((y_true - y_pred)**2)
	val = (1 - RSS/TSS)
    return val

