# runtime: O(n)
# space: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_valid_palindrome(s: str) -> bool:
            left = 0
            right = len(s)-1

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        processed_s = ''.join([c.lower() for c in s if c.isalnum()])
        return is_valid_palindrome(processed_s)

