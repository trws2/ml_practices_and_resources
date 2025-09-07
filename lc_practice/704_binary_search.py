# runtime: O(log(n))
# space: O(n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if  nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return -1

