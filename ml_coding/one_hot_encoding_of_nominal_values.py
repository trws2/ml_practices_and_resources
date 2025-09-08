import numpy as np

def to_categorical(x, n_col=None):
    m = {}    
    if n_col is None:
        a = np.sort(np.unique(x))
        a_size = len(a)
    else:
        a_size = n_col
        a = np.arange(a_size)

    for i, v in enumerate(a):
        vector = np.zeros((1, a_size))
        vector[0][i] = 1
        m[v] = vector.tolist()

    ret = []
    for i in x.tolist():
        ret.append(m[i])
    return ret


print(to_categorical(np.array([0, 1, 2, 1, 0])))

