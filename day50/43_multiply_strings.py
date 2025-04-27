# runtime: O(|num1| x |num2|)
# space: O(1)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]

        ret = 0
        for i1, c1 in enumerate(num1):
            for i2, c2 in enumerate(num2):
                tmp = int(c1) * int(c2) * (10**i1) * (10**i2)
                ret += tmp

        return str(ret)

