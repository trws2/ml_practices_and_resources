import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def compute_distance_square(p: List[int]) -> int:
            return p[0] ** 2 + p[1] ** 2

        min_heap = []
        for p in points:
            neg_distance_sq = -compute_distance_square(p)
            if len(min_heap) < k:
                heapq.heappush(min_heap, (neg_distance_sq, p))
            else:
                if min_heap[0][0] < neg_distance_sq:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (neg_distance_sq, p))
        
        return [x[1] for x in min_heap]

