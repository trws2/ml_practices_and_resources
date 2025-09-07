# runtime: O(n)
# space: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        for i in range(1, len(nums), 1):
            ans[i] = ans[i-1] * nums[i-1]
        
        right_product = 1
        for i in range(len(nums)-2, -1, -1):
            right_product *= nums[i+1]
            ans[i] *= right_product
        
        return ans

