
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        ws = 0
        max_sum = 0

        for i in range(n):
            mp[nums[i]] += 1
            ws += nums[i]

            if i >= k:
                le = nums[i - k]
                mp[le] -= 1
                ws -= le
                if mp[le] == 0:
                    del mp[le]

            if i >= k - 1 and len(mp) == k:
                max_sum = max(max_sum, ws)

        return max_sum

