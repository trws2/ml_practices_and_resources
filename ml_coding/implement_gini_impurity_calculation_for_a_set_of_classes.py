
import numpy as np

def gini_impurity(y):
    tmp = np.array(y)
    _, count = np.unique(tmp, return_counts=True)
    prob = count / len(tmp)
    val = 1 - sum(prob**2)
    return round(val,3)

y = [0, 0, 0, 0, 1, 1, 1, 1]
print(gini_impurity(y))

