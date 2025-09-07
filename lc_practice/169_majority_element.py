# runtime: O(n)
# space: O(n)
# this is another O(1) solution using Boyer-Moore Voting algorithm; see https://docs.google.com/presentation/d/1r7R3k3tX_48mjvwPzXUIMK9ETDa2ux7r1tPCwarQCgU/edit#slide=id.gef9b2294c7_0_0

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        ret = 0
        max_f = -1
        for c, f in nums_counter.items():
            if f > max_f:
                ret = c
                max_f = f
        return ret
