# runtime: O(nlog(n))
# space: O(n) 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort the array in ascending order
        nums_sorted = sorted(nums)

        left, right = self.twoSumSorted(nums_sorted, target)

        # scan original array to find left and right indices
        for i, n in enumerate(nums):
            if left == n:
                left_i = i

        for i, n in enumerate(nums):
            if i == left_i:
                continue
            if right == n:
                right_i = i

        return [left_i, right_i]


    def twoSumSorted(self, nums: List[int], target: int) -> List[int]:
        # use two pointers to scan from left and right
        left = 0
        right = len(nums)-1
        # if nums[left] + nums[right] == target, return the indices
        # if nums[left] + nums[right] < target, increment left by 1
        # if nums[left] + nums[right] > target, decrement right by 1
        while nums[left] + nums[right] != target:
            val = nums[left] + nums[right]
            if val < target:
                left += 1
            elif val > target:
                right -= 1

        return [nums[left], nums[right]]

