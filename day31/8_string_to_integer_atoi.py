# runtime: O(n)
# space: O(n)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        if not (s[0] in ('+', '-') or s[0].isdigit()):
            return 0

        sign = '-' if s[0] == '-' else ''
        if s[0] in ('+', '-'):
            s = s[1:]

        parsed_s = []
        for c in s:
            if c.isdigit():
                parsed_s.append(c)
            else:
                break
        
        parsed_s = "".join(parsed_s)
        try:
            ret = int(parsed_s)
        except:
            return 0

        if sign == '-':
            ret = -ret
            if ret < -2**31:
                ret = -2**31
        else:
            if ret > 2**31 - 1:
                ret = 2**31 - 1

        return ret
