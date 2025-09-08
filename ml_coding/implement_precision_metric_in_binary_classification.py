import numpy as np
def precision(y_true, y_pred):
    return sum(y_true[y_pred == 1]) / sum(y_pred == 1)

