# runtime: O(n)
# space: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window approach and maintain a hashmap containing
        # the current substring character and their associated position
        # for each new char scanned, if it does not overlap with existing
        # chars in the substring, add it to the hashmap. if it overlaps,
        # find the position of the overlapping char, update its position
        # in the hashmap, update starting position of substring, and update
        # current max length of substring if needed. keep iterating until 
        # all chars in the original string are scanned.

        if not s:
            return 0

        start = 0
        char_to_pos = {}
        ret = 0
        for i, c in enumerate(s):
            if c not in char_to_pos:
                char_to_pos[c] = i
                ret = max(ret, i-start+1)
                # print(f"A: char_to_pos={char_to_pos}, ret={ret}, start={start}")
                continue

            pos = char_to_pos[c]
            if pos < start: # not within the current max length substring
                char_to_pos[c] = i
                ret = max(ret, i-start+1)
                # print(f"B: char_to_pos={char_to_pos}, ret={ret}, start={start}")
                continue

            # reset start position            
            start = pos+1
            char_to_pos[c] = i
            ret = max(ret, i-start+1)
            # print(f"C: char_to_pos={char_to_pos}, ret={ret}, start={start}")

        return ret

