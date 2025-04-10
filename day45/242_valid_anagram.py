# runtime: O(|s| + |t|)
# space: O(|s| + |t|)

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = Counter(s)
        tc = Counter(t)

        for c, f in sc.items():
            if not (c in tc and tc.get(c, -1) == f):
                return False

        for c, f in tc.items():
            if not (c in tc and sc.get(c, -1) == f):
                return False

        return True
