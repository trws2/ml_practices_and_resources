# runtime: O(log(n))
# space: O(n)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = int((left+right)/2)
            mid_val = nums[mid]
            left_val = nums[left]
            right_val = nums[right]

            if mid_val == target:
                return mid

            if left_val <= mid_val:
                if left_val <= target <= mid_val:
                    return self.binarySearch(nums, target, left, mid)
                else:
                    left = mid+1
            else:
                if mid_val <= target <= right_val:
                    return self.binarySearch(nums, target, mid, right)
                else:
                    right = mid-1

        return -1

        
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = int((left+right)/2)
            mid_val = nums[mid]

            if mid_val == target:
                return mid
            if mid_val < target:
                left = mid+1
            else:
                right = mid-1

        return -1

