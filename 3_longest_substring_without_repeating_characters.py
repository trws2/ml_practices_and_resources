class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        start = 0
        char_to_pos = {}
        ret = 0
        for i, c in enumerate(s):
            if c not in char_to_pos:
                char_to_pos[c] = i
                ret = max(ret, i-start+1)
                continue

            pos = char_to_pos[c]
            if pos < start: # not within the current max length substring
                char_to_pos[c] = i
                ret = max(ret, i-start+1)
                continue

            # reset start position            
            start = pos+1
            char_to_pos[c] = i
            ret = max(ret, i-start+1)

        return ret

