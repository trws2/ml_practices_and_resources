# runtime: O(n^3)
# space: O(n^3)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_len = 1
        max_s = s[0]
        for i in range(len(s)):
            for j in range(i+max_len, len(s)):
                sub_s = s[i:j+1]
                if max_len < len(sub_s) and sub_s == sub_s[::-1]:
                    max_len = len(sub_s)
                    max_s = sub_s

        return max_s

