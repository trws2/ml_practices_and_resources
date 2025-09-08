import numpy as np

def dice_score(y_true, y_pred):
    a = y_true == 1
    b = y_pred == 1
    inter = np.sum(a & b)
    union = np.sum(a) + np.sum(b)
    if union == 0:
        return 0.0

    res = 2 * inter / union
    return round(res, 3)


y_true = np.array([1, 1, 0, 0])
y_pred = np.array([1, 1, 0, 0])
print(dice_score(y_true, y_pred))

