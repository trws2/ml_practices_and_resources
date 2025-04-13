# runtime: O(n)
# space: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_nums = [1]
        new_nums.extend(nums)
        new_nums.append(1)

        def cumsum(nums_in):
            ret = []
            for i, n in enumerate(nums_in):
                if i == 0:
                    ret.append(nums_in[0])
                else:
                    ret.append(nums_in[i] * ret[-1])
            return ret
        
        left_to_right = cumsum(new_nums)
        right_to_left = cumsum(new_nums[::-1])
        right_to_left = right_to_left[::-1]

        ret = []
        for i in range(1, len(left_to_right)-1):
            ret.append(left_to_right[i-1] * right_to_left[i+1])

        return ret

