# from https://www.tryexponent.com/questions/3489/implement-k-nearest-neighbors-algorithm

import numpy as np
import heapq

def knn(X_train, y_train, X_new, k):
  if len(np.unique(y_train)) != 2:
    raise Exception("must contain 2 labels")

  dist_sq_list = np.sum((X_train - X_new) ** 2, axis=1)
  heap_based_solution = True
  if heap_based_solution:

    tuples = [(d, y) for d, y in zip(dist_sq_list, y_train)]
    heap = []
    for t in tuples:
      neg_dist_sq = -t[0]
      y = t[1]

      if len(heap) == k:
        if neg_dist_sq > heap[0][0]:
          heapq.heappop(heap)
          heapq.heappush(heap, (neg_dist_sq, y))
        else:
          continue
      else:
        heapq.heappush(heap, (neg_dist_sq, y))
    top_k_labels = [t[1] for t in heap]
  else:
    tuples = [(d, y) for d, y in zip(dist_sq_list, y_train)]
    tuples.sort(key = lambda x: (x[0], x[1]))
    tuples = tuples[:k]
    top_k_labels = [t[1] for t in tuples]

  if sum(top_k_labels) > (k / 2.0):
    return 1
  else:
    return 0

X_train = np.array([[1, 2], [2, 3], [3, 4], [6, 7], [7, 8], [8, 9]])
y_train = np.array([0, 0, 0, 1, 1, 1])

X_new = np.array([2, 2]) # The new point we want to classify
k = 3 # We'll look at the 3 closest points

y_pred = knn(X_train, y_train, X_new, k) # should return 0    
print(y_pred)
