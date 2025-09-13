class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums
        from sortedcontainers import SortedList
        li = SortedList()
        res = []
        for i in range(len(nums)):
            li.add(nums[i])
            if len(li) > k:
                li.remove(nums[i-k])
            if len(li) == k:
                median = li[k//2] if k%2 == 1 else (li[k//2] + li[k//2 - 1]) / 2
                res.append(median)
        return res

