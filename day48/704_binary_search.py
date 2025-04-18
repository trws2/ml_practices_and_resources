# the following 2 solutions both work
# runtime: O(log(n))
# space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
                continue
            
            right = mid - 1
        
        return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums)-1

        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
                continue

            right = mid

        if nums[left] == target:
            return left

        return -1


