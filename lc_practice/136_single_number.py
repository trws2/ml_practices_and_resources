# runtime: O()
# space: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = set()
        for n in nums:
            if n in tmp:
                tmp.remove(n)
            else:
                tmp.add(n)
        return list(tmp)[0]

