# runtime: O(n)
# space: O(n)

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ret = ','.join([str(len(s)) for s in strs])
        ret += '#'
        ret += ''.join([s for s in strs])
        return ret


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        s_split = s.split('#')
        sz = s_split[0]
        sz = [int(l) for l in sz.split(',')]

        s = s[len(s_split[0])+1:]
        ret = []
        index = 0
        i = 0
        while i < len(sz):
            ret.append(s[index:index+sz[i]])
            index = index+sz[i]            
            i += 1

        return ret

