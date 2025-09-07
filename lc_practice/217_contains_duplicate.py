# runtime: O(n)
# space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)

        if len(set_nums) == len(nums):
            return False

        return True

