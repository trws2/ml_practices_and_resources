# runtime: O(n)
# space: O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums[:])
        return nums
