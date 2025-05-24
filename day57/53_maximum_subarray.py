# runtime: O(n)
# space: O(1)

# newer implementation
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # define
        # f(0) = nums[0]
        # for i > 0, f(i) = f(i-1) + nums[i] if f(i-1) + nums[i] > nums[i] else nums[i]

        ret = None
        prev = None
        for i in range(len(nums)):
            if i == 0:
                ret = nums[0]
                prev = nums[0]
            else:
                if prev + nums[i] > nums[i]:
                    curr = prev + nums[i]
                else:
                    curr = nums[i]
                if curr > ret:
                    ret = curr
                prev = curr

        return ret

# older implementation
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # define f[i] such as f[i] = f[i-1] + nums[i] if f[i-1] > 0 else nums[i]
        
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i-1] + nums[i], nums[i])

        return max(f)

