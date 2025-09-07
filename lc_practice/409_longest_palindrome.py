# runtime: O(n)
# space: O(|chars|)

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)

        mod_2_counter = {}
        has_remainder = False
        for c, f in s_counter.items():
            remainder = f % 2
            mod_2_counter[c] = f - remainder
            if remainder > 0:
                has_remainder = True
        
        ret = 1 if has_remainder else 0
        for c, f in mod_2_counter.items():
            ret += f
        
        return ret

