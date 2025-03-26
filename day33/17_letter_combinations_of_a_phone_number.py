# runtime: O(|digits|)
# space: O(|digits|)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            2: list('abc'),
            3: list('def'),
            4: list('ghi'),
            5: list('jkl'),
            6: list('mno'),
            7: list('pqrs'),
            8: list('tuv'),
            9: list('wxyz'),
        }
        
        l = []
        for d in digits:
            l.append(digit_map[int(d)])

        if not l:
            return []

        ret = l[0]
        if len(l) == 1:
            return ret

        for i, e_list in enumerate(l):
            if i == 0:
                continue
            
            new_ret = []
            for r in ret:
                for c in e_list:
                    tmp = r + c
                    new_ret.append(tmp)

            ret = new_ret

        return ret
