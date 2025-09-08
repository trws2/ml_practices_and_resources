import numpy as np

def calculate_f1_score(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)    

    a = y_pred == 1
    b = y_true == 1

    if sum(b) == 0:
        return 0.0

    prec = sum(a & b) / sum(a)
    recall = sum(a & b) / sum(b)

    f1 = 2 * prec * recall / (prec + recall)

	return round(f1,3)

