# runtime: O(2^n)
# space: O(2^n) 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []
        cur = []
        for i in range(n):
            cur.append([i])
        ret.extend(cur[:])

        while True:
            prev = cur
            cur = []
            for e in prev:
                idx = e[-1] + 1
                while idx < n:
                    new = e[:]
                    new.append(idx)
                    cur.append(new)
                    idx += 1
            if not cur:
                break
            ret.extend(cur[:])    

        final_ret = [[]]
        for e in ret:
            v = []
            for i in e:
                v.append(nums[i])
            final_ret.append(v)

        return final_ret
