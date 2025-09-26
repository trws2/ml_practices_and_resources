
import numpy as np
from typing import Tuple

def kmeans(X: np.ndarray, K: int, max_iters: int, random_state: int=42, eps: float=1e-5) -> Tuple[np.ndarray, np.ndarray, bool]:
    def within_cluster_sum_of_square(centroids: np.ndarray, X: np.ndarray, assignments: np.ndarray):
        wcss = 0
        for i in range(K):
            sel = assignments == i
            if sum(sel) == 0:
                continue
            wcss += np.sum(np.sum((X[sel, :] - centroids[i, :]) ** 2, axis=1))

        return wcss

    # np.random.seed(random_state)
    min_val = np.min(X)
    max_val = np.max(X)
    num_points, feat_dim = X.shape

    print(f"min_va={min_val}, max_val={max_val}, num_points={num_points}, feat_dim={feat_dim}")

    centroids = np.random.uniform(low=min_val, high=max_val, size=(K, feat_dim))
    prev_wcss = -1

    for i in range(max_iters):
        # compute distance between each point and centroids
        dist_sq_matrix = np.zeros((K, num_points))
        for j in range(K):
            dist_sq_matrix[j, :] = np.sum((X - centroids[j, :])**2, axis=1) 

        # compute assignments
        assignments = np.argmin(dist_sq_matrix, axis=0)

        # compute new centroids
        new_centroids = np.zeros((K, feat_dim))
        for j in range(K):
            sel = assignments == j
            if sum(sel) == 0:
                # no point found
                new_centroids[j,:] = centroids[j, :]
            else:
                new_centroids[j,:] = np.mean(X[sel, :], axis=0)

        # compute new centroids difference
        # diff = np.mean(np.sqrt(np.sum((centroids - new_centroids)**2, axis=1)))
        centroids = new_centroids
        if i == 0:
            continue

        # stop if avg difference < eps
        wcss = within_cluster_sum_of_square(centroids, X, assignments)
        diff = abs(wcss - prev_wcss)

        print(f"iter={i}, wcss={wcss}, diff={diff}")
        if diff < eps:
            return new_centroids, assignments, True

        prev_wcss = wcss

    return centroids, assignments, False



if __name__ == "__main__":
  X = np.array([[-1, -1], [0, 0], [1, 1]])
  K = 3
  max_iters = 50
  centroids, assignments, converged = kmeans(X, K, max_iters=max_iters, random_state=0)
  print(f"X={X}")
  print(f"centroids={centroids}")
  print(f"assignments={assignments}")
  print(f"converged={converged}")  


  X1 = np.random.randn(10, 2) - 1
  X2 = np.random.randn(10, 2)
  X3 = np.random.randn(10, 2) + 1
  X = np.concatenate((X1, X2, X3), axis=0)
  K = 3
  max_iters = 50
  centroids, assignments, converged = kmeans(X, K, max_iters=max_iters)
  print(f"X={X}")
  print(f"centroids={centroids}")
  print(f"assignments={assignments}")
  print(f"converged={converged}")  



