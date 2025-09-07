# runtime: log(n)
# space: log(n)  # for recursive function call solution

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        if n == 0:
            return 1

        def calc_pow(x, n):
            if n == 0:
                return 1

            if n == 1:
                return x

            res = calc_pow(x, n // 2)
            res *= res

            if n % 2 == 1:
                res *= x

            return res
        
        return calc_pow(x, n)

