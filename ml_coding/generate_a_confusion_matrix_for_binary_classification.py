import numpy as np

def confusion_matrix(data):
    y_true = np.array([x[0] for x in data])
    y_pred = np.array([x[1] for x in data])

	tp = sum((y_true == 1) & (y_pred == 1))
    fn = sum((y_true == 1) & (y_pred == 0))
    fp = sum((y_true == 0) & (y_pred == 1))
    tn = sum((y_true == 0) & (y_pred == 0))

    return [[tp, fn], [fp, tn]]

