# runtime: O(n)
# space: O(n)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # define f[i] such as f[i] = f[i-1] + nums[i] if f[i-1] > 0 else nums[i]
        
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i-1] + nums[i], nums[i])

        return max(f)

