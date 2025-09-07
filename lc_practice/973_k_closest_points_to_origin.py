# runtime: O(nlog(k))
# space: O(n)

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for each point, compute its negative square sum
        dist_to_point_list = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            dist = -dist
            dist_to_point_list.append((dist, point))

        # maintain a heap data structure to add square sum along with their points to the heap
        min_heap = []
        
        for item in dist_to_point_list:
            heapq.heappush(min_heap, item)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # for a given k, pop the element from the heap till k is reached and return all the associated
        # points.
        ret = []
        while min_heap:
            item = heapq.heappop(min_heap)
            ret.append(item[1])
        return ret

