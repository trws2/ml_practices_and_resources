import numpy as np

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    # 1. compute distances of each point to centroids
    # 2. assign each point to its closest centroid.
    # 3. points belonging to the same centroid form a cluster, and
    #    compute the new cluster centroid
    # 4. if the new centroids are within a thresholded distance difference
    #    old centroids, we stop the process and return the new centroids as 
    #    results 
    # 5. we go back to step 1 and repeat the process.

    points = np.array(points)
    centroids = np.array(initial_centroids)

    old_assignment = {}
    new_assignment = {}
    iterations = 0
    while True:
        iterations += 1
        for r_id in range(points.shape[0]):
            point = points[r_id]
            dist_sq = np.sum(np.square((point - centroids)), axis=1)

            cluster_id = np.argmin(dist_sq)
            dist = np.min(dist_sq)
            new_assignment[r_id] = (cluster_id, dist)

        # compute new assignment distance to centroid difference sum
        if len(old_assignment) == 0:
            old_assignment = new_assignment
            new_assignment = {}
        else:
            old_avg_dist = np.mean([x[1] for x in old_assignment.values()])
            new_avg_dist = np.mean([x[1] for x in new_assignment.values()])

            delta = abs(new_avg_dist - old_avg_dist) / old_avg_dist
            if delta < 0.01:
                # print(f"k-means converages after {iterations} iterations, new_avg_dist={new_avg_dist}, old_avg_dist={old_avg_dist}, delta={delta}")
                break

    # compute final centroids
    final_centroids = []
    k = len(initial_centroids)
    for i in range(k):
        cluster_points = []
        for point_id, cluster_info in new_assignment.items():
            cluster_id = cluster_info[0]
            if cluster_id != i:
                continue
            cluster_points.append(points[point_id])

        # print(f"cluster {i} has {len(cluster_points)} points, np.array(cluster_points)={np.array(cluster_points)}")
        cluster_centroid = np.mean(np.array(cluster_points), axis=0).tolist()
        final_centroids.append(tuple(cluster_centroid))

    return array_round(final_centroids)


def array_round(l: list[list[float, float]]):
    for i in range(len(l)):
        l[i] = tuple(round(x, 4) for x in l[i])
    return l

if __name__ == "__main__":
    ans1 = k_means_clustering([(1, 2), (1, 4), (1, 0), (10, 2), (10, 4), (10, 0)], 2, [(1, 1), (10, 1)], 10)
    ans2 = k_means_clustering([(0, 0, 0), (2, 2, 2), (1, 1, 1), (9, 10, 9), (10, 11, 10), (12, 11, 12)], 2, [(1, 1, 1), (10, 10, 10)], 10)
    ans3 = k_means_clustering([(1, 1), (2, 2), (3, 3), (4, 4)], 1, [(0,0)], 10)
    ans4 = k_means_clustering([(0, 0), (1, 0), (0, 1), (1, 1), (5, 5), (6, 5), (5, 6), (6, 6),(0, 5), (1, 5), (0, 6), (1, 6), (5, 0), (6, 0), (5, 1), (6, 1)], 4, [(0, 0), (0, 5), (5, 0), (5, 5)], 10)

    print(ans1)
    assert(ans1 == [(1.0, 2.0), (10.0, 2.0)])
    print(ans2)
    assert(ans2 == [(1.0, 1.0, 1.0), (10.3333, 10.6667, 10.3333)])
    print(ans3)
    assert(ans3 == [(2.5, 2.5)])
    print(ans4)
    assert(ans4 == [(0.5, 0.5), (0.5, 5.5), (5.5, 0.5), (5.5, 5.5)])



