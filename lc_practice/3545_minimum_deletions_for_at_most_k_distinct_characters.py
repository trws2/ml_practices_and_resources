from collections import Counter
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        chars = [c for c in s]
        counter = Counter(chars)

        seq = [(freq, c) for c, freq in counter.items()]
        seq.sort(key=lambda x: (x[0], x[1]), reverse=True)
        ans = 0
        for i in range(k, len(seq)):
            ans += seq[i][0]
        return ans
        
