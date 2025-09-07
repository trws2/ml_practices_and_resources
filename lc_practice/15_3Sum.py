# runtime: O(n^2)
# space: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return res


# the following solution use rely on 2sum to solve it
# runtime: O(n^2)
# space: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        size = len(nums)
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i != 0 and n == nums[i-1]:
                continue
            res.extend(self.twoSum(nums, i+1, size, -n))
        return res

    def twoSum(self, nums: List[int], left: int, right: int, target: int) -> List[List[int]]:
        res = []        
        s = set()
        i = left
        while i < right:
            new_num = nums[i]
            if (target - new_num) in s:
                # found a triplet
                res.append([-target, new_num, target - new_num])
                while i < right-1 and nums[i] == nums[i+1]:
                    i += 1
            s.add(new_num)
            i += 1
        return res

