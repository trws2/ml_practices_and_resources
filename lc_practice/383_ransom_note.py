# runtime: O(n)
# space: O(n)

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_counter = Counter(ransomNote)        
        magazine_counter = Counter(magazine)

        for c, f in ransomNote_counter.items():
            if c not in magazine_counter:
                return False
            if f > magazine_counter.get(c):
                return False
        
        return True

