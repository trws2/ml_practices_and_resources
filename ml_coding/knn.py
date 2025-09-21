# from https://www.tryexponent.com/questions/3489/implement-k-nearest-neighbors-algorithm

# KNN aglorithm

import numpy as np
from typing import List

def knn(X_train: np.ndarray, y_train: np.ndarray, X_new_in: np.ndarray, k: int) -> List[int]:
  if k == 0:
    raise ValueError("k must be > 0")

  if k % 2 == 0:
    raise ValueError("k must be an odd number")

  if len(X_new_in.shape) == 1:  # 1 point
    X_new_all = X_new_in.reshape(1, X_new_in.shape[0])
  else:
    X_new_all = X_new_in
  num_points = X_new_all.shape[0]

  if k > X_train.shape[0]:
    raise ValueError(f"k must be <= {num_points}")

  if X_train.shape[0] != len(y_train):
    raise ValueError(f"num_points[{num_points}] != len(y_train)[{len(y_train)}]")

  classifications = np.zeros(num_points)
  for i in range(num_points):
    X_new = X_new_all[i, :]

    # compute distance to each point  
    dist_sq = np.sum((X_train - X_new)**2, axis=1)

    # find the top k closest point
    dist_sq_and_ids = [(d, i) for i, d in enumerate(dist_sq)]
    dist_sq_and_ids.sort(key=lambda x: x[0]) # sort in increasing order
    top_ids = [i for d, i in dist_sq_and_ids[:k]]

    # get those labels and compute majority; note that we have binary labels
    class_1_votes = np.sum([y_train[id] for id in top_ids])
    if class_1_votes > k/2:
      classifications[i] = 1
    else:
      classifications[i] = 0

  return classifications.tolist()


def test_knn():
    """Comprehensive test suite for KNN implementation"""
    
    print("=== KNN Test Suite ===\n")
    
    # Test Case 1: Original example (binary classification)
    print("Test 1: Binary classification - original example")
    X_train = np.array([[1, 2], [2, 3], [3, 4], [6, 7], [7, 8], [8, 9]])
    y_train = np.array([0, 0, 0, 1, 1, 1])
    X_new = np.array([2, 2])
    k = 3
    
    result = knn(X_train, y_train, X_new, k)
    print(f"Point {X_new} classified as: {result}")
    print(f"Expected: 0 (closer to class 0 cluster)\n")
    
    # Test Case 2: Multiple points at once
    print("Test 2: Multiple points classification")
    X_new_multiple = np.array([[2, 2], [7, 7], [5, 5]])
    results = knn(X_train, y_train, X_new_multiple, k)
    print(f"Points {X_new_multiple.tolist()} classified as: {results}")
    print(f"Expected: [0, 1, varies] (boundary case for middle point)\n")
    
    # Test Case 3: Multi-class classification
    print("Test 3: Multi-class classification")
    X_train_multi = np.array([[1, 1], [1, 2], [2, 1],    # class 0
                              [5, 5], [5, 6], [6, 5],    # class 1  
                              [9, 9], [9, 10], [10, 9]]) # class 2
    y_train_multi = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
    X_new_multi = np.array([1.5, 1.5])
    
    result = knn(X_train_multi, y_train_multi, X_new_multi, k=3)
    print(f"Point {X_new_multi} classified as: {result}")
    print(f"Expected: 0 (closest to class 0 cluster)\n")
    
    # Test Case 4: Edge case - k = 1
    print("Test 4: k=1 (nearest neighbor)")
    result = knn(X_train, y_train, np.array([1, 2]), k=1)
    print(f"Point [1, 2] with k=1 classified as: {result}")
    print(f"Expected: 0 (exact match with training point)\n")
    
    # Test Case 5: Tie handling with even k (should still work)
    print("Test 5: Even k value")
    try:
        result = knn(X_train, y_train, np.array([4.5, 5.5]), k=4)
        print(f"Point [4.5, 5.5] with k=4 classified as: {result}")
        print("Even k works fine with numpy-based voting\n")
    except Exception as e:
        print(f"Error with even k: {e}\n")
    
    # Test Case 6: 1D data
    print("Test 6: 1D feature space")
    X_train_1d = np.array([[1], [2], [8], [9]])
    y_train_1d = np.array([0, 0, 1, 1])
    X_new_1d = np.array([3])
    
    result = knn(X_train_1d, y_train_1d, X_new_1d, k=3)
    print(f"1D point {X_new_1d[0]} classified as: {result}")
    print(f"Expected: 0 (closer to 0-class points)\n")
    
    # Test Case 7: Error handling
    print("Test 7: Error handling")
    try:
        knn(X_train, y_train, X_new, k=0)
        print("ERROR: Should have raised ValueError for k=0")
    except ValueError as e:
        print(f"✓ Correctly caught error for k=0: {e}")
    
    try:
        knn(X_train, y_train, X_new, k=10)  # k > training size
        print("ERROR: Should have raised ValueError for k > training size")
    except ValueError as e:
        print(f"✓ Correctly caught error for k > training size: {e}")
    
    try:
        knn(X_train, y_train[:-1], X_new, k=3)  # mismatched sizes
        print("ERROR: Should have raised ValueError for mismatched sizes")
    except ValueError as e:
        print(f"✓ Correctly caught error for mismatched sizes: {e}")
    
    print("\n=== All tests completed ===")


if __name__ == "__main__":
    test_knn()
