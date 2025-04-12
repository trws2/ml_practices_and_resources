# runtime: O(n)
# space: O(n)

# solution 1:
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        thres = int(len(nums) / 2)
        for n, f in counter.items():
            if f > thres:
                return n

        return -1


# solution 2:
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        ret = 0
        majority = 0

        for n in nums:
            hash[n] = 1 + hash.get(n, 0)
            if hash[n] > majority:
                ret = n
                majority = hash[n]

        return ret
