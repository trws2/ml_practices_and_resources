import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    np.random.seed(42)
    num_samples = X.shape[0]
    inds = np.arange(num_samples)
    np.random.shuffle(inds)

    ret = []
    for start in range(0, num_samples, batch_size):
        end = start + batch_size
        print(inds[start:end])

        cur_X = X[inds[start:end]]
        cur_y = y[inds[start:end]]

        ret.append([cur_X.tolist(), cur_y.tolist()])
    
    return ret


print(batch_iterator(np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), np.array([1, 2, 3, 4, 5]), batch_size=2))



