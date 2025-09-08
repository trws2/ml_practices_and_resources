import numpy as np

def shuffle_data(X, y, seed=None):
    np.random.seed(seed)
    inds = [i for i in range(len(y))]
    np.random.shuffle(inds)
    X = X[inds]
    y = y[inds]
    return X, y

