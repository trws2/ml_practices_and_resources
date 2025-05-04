# this linear time solution works

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        occur = defaultdict(int)
        prev_char = s[0]

        for char in s:
            if char != prev_char:
                count += min(occur['0'], occur['1'])
                occur[char] = 1
            else:
                occur[char] = occur[char] + 1
            
            prev_char = char
        count += min(occur['0'], occur['1'])
        return count



# the following solution run of time.
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        index_to_map = {}
        m = {}
        m['0'] = 0
        m['1'] = 0
        for i, c in enumerate(s):
            m[c] += 1
            index_to_map[i] = dict(m)

        res = 0
        for i in range(len(s)):
            i_map = index_to_map[i]
            for j in range(i+1, len(s)):
                sub_str_len = (j-i)+1
                if sub_str_len % 2 != 0:
                    continue

                j_map = index_to_map[j]
                count_0s = j_map['0'] - i_map['0']
                count_1s = j_map['1'] - i_map['1']
                if s[i] == '0':
                    count_0s += 1
                else:
                    count_1s += 1                    

                if count_0s == count_1s:
                    sub_str = s[i:j+1]
                    a = '0' * int(sub_str_len / 2)
                    b = '1' * int(sub_str_len / 2)
                    target_str1 = a + b
                    target_str2 = b + a                    
                    if sub_str in (target_str1, target_str2):
                        res += 1

        return res
