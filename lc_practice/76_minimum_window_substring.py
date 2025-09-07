# runtime: O(|s| + |t|)
# space: O(|s| + |t|)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        char_count = defaultdict(int)
        for ch in t:
            char_count[ch] += 1

        target_chars_remaining = len(t)
        min_window = (0, float("inf"))
        start_index = 0

        for end_index, ch in enumerate(s):
            if char_count[ch] > 0:
                target_chars_remaining -= 1
            char_count[ch] -= 1

            if target_chars_remaining == 0:
                while True:
                    char_at_start = s[start_index]
                    if char_count[char_at_start] == 0:
                        break
                    char_count[char_at_start] += 1
                    start_index += 1

                if end_index - start_index <  min_window[1] - min_window[0]:
                    min_window = (start_index, end_index)

                char_count[s[start_index]] += 1
                target_chars_remaining += 1
                start_index += 1

        return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1]


# solution passing simple test cases but running out of time on long s and t

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def s_contains_t(s, t):
            for c, f in t.items():
                if f > s[c]: # frequency in t is greater that frequency in s
                    return False
            return True

        freq_count_t = Counter(list(t))
        min_len = float("inf")
        min_str = ""
        for i in range(len(s)):
            start_id = i+len(t)
            for j in range(start_id, len(s)+1): # j means the ending index not including the last char.
                if j == start_id:
                    freq_count_cur_s = Counter(list(s[i:j]))
                else:
                    freq_count_cur_s[s[j-1]] += 1                    
                if s_contains_t(freq_count_cur_s, freq_count_t):
                    if min_len > (j-i):
                        min_str = s[i:j]
                        min_len = (j-i)
                    break
        
        return min_str

