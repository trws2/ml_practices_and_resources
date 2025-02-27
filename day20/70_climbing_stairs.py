# runtime: O(n)
# space: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        ways_1 = 1
        ways_2 = 1
        ret = 1
        for i in range(2, n+1):
            ret = ways_1 + ways_2
            ways_2 = ways_1            
            ways_1 = ret
        return ret

        # ways = [0] * (n+1)
        # ways[0] = 1
        # ways[1] = 1
        # for i in range(2, n+1):
        #     ways[i] = ways[i-1] + ways[i-2]
        # return ways[n]

