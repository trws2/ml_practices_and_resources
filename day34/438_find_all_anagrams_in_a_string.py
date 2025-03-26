# runtime: O(|s| x |p|)
# space: O(|s|)

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        t = Counter(p)
        for i in range(len(s)):
            if i == 0:
                sub_str = s[i:i+len(p)]
                c = Counter(sub_str)
                if c == t:
                    ret.append(i)
            else:
                c[s[i-1]] -= 1
                if i+len(p)-1 < len(s):
                    c[s[i+len(p)-1]] += 1
                else:
                    break
                if c == t:
                    ret.append(i)                
        return ret 

