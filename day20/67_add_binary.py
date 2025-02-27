# runtime: O(n)
# space: O(n)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_chars = list(a)
        b_chars = list(b)

        a_len = len(a_chars)
        b_len = len(b_chars)
        max_len = max(len(a_chars), len(b_chars))
        n = -1

        carry = 0
        ret = []
        while n >= -max_len:
            a_char = 0
            b_char = 0

            if n >= -a_len:
                a_char = int(a_chars[n])
            if n >= -b_len:
                b_char = int(b_chars[n])

            s = a_char + b_char + carry
            r = s % 2
            carry = int(s / 2)

            n -= 1

            ret.append(str(r))

        if carry > 0:
            ret.append('1')

        return "".join(ret[::-1])
