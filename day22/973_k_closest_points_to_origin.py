# runtime: O(nlog(k)), where k is the number of distinct distance square, which is less than n
# space: O(n)

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for each point, compute its square sum
        dist_to_point_map = {}
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            if dist not in dist_to_point_map:
                dist_to_point_map[dist] = []
            dist_to_point_map[dist].append(point)        
        dist_to_point_list = [(k, v) for k, v in dist_to_point_map.items()]
        print(dist_to_point_list)

        # maintain a heap data structure to add square sum along with their points to the heap
        min_heap = []

        for item in dist_to_point_list:
            heapq.heappush(min_heap, item)

        # for a given k, pop the element from the heap till k is reached and return all the associated
        # points.

        ret = []
        while min_heap:
            item = heapq.heappop(min_heap)
            ret.extend(item[1])
            if len(ret) >= k:
                ret = ret[:k]
                break
        return ret
