# runtime: O(n)
# space: O(n)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cs = Counter(s)
        ct = Counter(t)

        for k, v in cs.items():
            if v != ct.get(k, -1):
                return False

        for k, v in ct.items():
            if v != cs.get(k, -1):
                return False
            
        return True
        

