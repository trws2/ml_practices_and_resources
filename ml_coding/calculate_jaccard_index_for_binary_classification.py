
import numpy as np

def jaccard_index(y_true, y_pred):
    A = (y_true == 1)
    B = (y_pred == 1)
    result = sum(A & B) / sum (A | B)
    return round(result, 3)

# Test case 1: Perfect match 
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 1, 0, 1])
print(jaccard_index(y_true, y_pred))

