# runtime: O(|str(x)|)
# space:O(|str(x)|)

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            ret = str(x)[1:]
            ret = ret[::-1]
            ret = -int(ret)
        else:
            ret = str(x)[::-1]
            ret = int(ret)

        if not (-2**31 <= ret <= 2**31 - 1):
            return 0
        
        return ret

