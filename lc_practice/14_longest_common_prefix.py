# runtime: O(m x n), where is shortest string length and m is number of strings
# space: O(|prefx|), where prefix is the returned prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def get_next_prefix_letter(strs: List[str], i: int) -> str:
            if not strs:
                return ''

            if i >= len(strs[0]):
                return ''
            
            c = strs[0][i]
            for j, s in enumerate(strs):
                if j == 0:
                    continue
                if i >= len(s):
                    return ''
                if c != s[i]:
                    return ''

            return c

        index = 0
        ret = []
        while True:
            c = get_next_prefix_letter(strs, index)
            if not c:
                break

            ret.append(c)
            index += 1

        return ''.join(ret)

