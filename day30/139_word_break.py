# runtime: 
# space: 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        cache = {}

        def wordBreakAux(s: str) -> bool:
            if s in word_set:
                return True

            if s in cache:
                return cache[s]

            cur_str = []
            for i, c in enumerate(s):
                cur_str.append(c)
                cur_s = "".join(cur_str)

                if cur_s in word_set:
                    remaining_str = s[i+1:]
                    res = wordBreakAux(remaining_str)
                    cache[remaining_str] = res
                    if res:
                        return True

            return False

        return wordBreakAux(s)

