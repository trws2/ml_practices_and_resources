import numpy as np

def f_score(y_true, y_pred, beta):
    beta_sq = beta**2
    prec = sum(y_true[y_pred == 1]) / sum(y_pred == 1)
    recall = sum(y_pred[y_true == 1]) / sum(y_true == 1)
    val = (1 + beta_sq) * prec * recall / (beta_sq * prec + recall)
    return round(val, 3)

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
beta = 1
print(f_score(y_true, y_pred, beta))

