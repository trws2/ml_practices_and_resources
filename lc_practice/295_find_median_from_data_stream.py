# runtime: addNum O(log(n)), findMedian: O(1)
# space: O(n)

class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        heappush(self.lo, -num)
        heappush(self.hi, -self.lo[0])
        heappop(self.lo)

        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)        

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (self.hi[0] - self.lo[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# new practice

import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # push into the right queue
        if len(self.right) == 0 or num <= self.right[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        #
        if len(self.left) > len(self.right) + 1:
            curr = -heapq.heappop(self.left)
            heapq.heappush(self.right, curr)
        elif len(self.right) > len(self.left):
            curr = heapq.heappop(self.right)
            heapq.heappush(self.left, -curr)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            ret = (-self.left[0] + self.right[0]) / 2
        else:
            ret = -self.left[0]
        return ret


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


