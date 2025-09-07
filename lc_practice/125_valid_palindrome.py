# runtime: O(n)
# space: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_s = ''.join([c.lower() for c in s if c.isalnum()])
        return self.isPalindromeAux(processed_s)

    def isPalindromeAux(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
