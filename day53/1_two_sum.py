# another implementation
# runtime: O(n x log(n))
# space: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def twoSumSorted(nums_sorted: List[int]) -> List[int]:
            left = 0
            right = len(nums_sorted) - 1

            while True:
                val = nums_sorted[left] + nums_sorted[right]
                if val == target:
                    return [nums_sorted[left], nums_sorted[right]]

                if val < target:
                    left += 1
                    continue

                if val > target:
                    right -= 1

        nums_sorted = sorted(nums)
        left_num, right_num = twoSumSorted(nums_sorted)

        for i, n in enumerate(nums):
            if left_num == n:
                left_index = i
                break

        for i, n in enumerate(nums):
            if left_index == i:
                continue
            if right_num == n:
                right_index = i
                break

        return [left_index, right_index]


# one implementation
# runtime: O(n)
# space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            remainer = target - n
            if remainer in m:
                return [i, m[remainer]]
            m[n] = i
        return []
            
