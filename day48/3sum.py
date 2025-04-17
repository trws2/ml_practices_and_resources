# runtime: 
# space: O(|solution triplets|)

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


# the following solution runs too long to pass all test cases for this problem
# runtime: O(n^3)
# space: O(|solution triplets|)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums: List[int], i: int, target: int) -> List[int]:
            ret = []
            start = i+1
            for j in range(start, len(nums)):
                if j > start and nums[j] == nums[j-1]:
                    continue
                remain = target - nums[j]
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[k] == remain:
                        ret.append([nums[i], nums[j], nums[k]])
            return ret

        nums = sorted(nums)
        ret = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            remain = 0 - nums[i]
            ret.extend(twoSum(nums, i, remain))

        return ret

