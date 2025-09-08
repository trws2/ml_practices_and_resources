import numpy as np
def recall(y_true, y_pred):
    return sum(y_pred[y_true == 1]) / sum(y_true[y_true == 1])

