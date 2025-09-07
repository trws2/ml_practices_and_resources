# runtime: O(target_sum x N)
# space: O(target_sum x N)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target_sum = int(total_sum / 2)
        len_nums = len(nums)

        dp = [[False for _ in range(target_sum+1)] for _ in range(len_nums+1)]
        for i in range(len_nums+1):
            dp[i][0] = True

        for i in range(1, len_nums+1):
            for j in range(1, target_sum+1):
                dp[i][j] = dp[i-1][j]
                if j-nums[i-1] >= 0:
                    dp[i][j] |= dp[i-1][j-nums[i-1]]

        return dp[len_nums][target_sum]
