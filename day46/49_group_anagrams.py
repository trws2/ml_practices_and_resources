# runtime: O(n x log(|s|))
# space: O(n x |s|)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)

        return list(ans.values())


# runtime: O(n^2 x |chars|)
# space: O(n x |chars|)

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        if not strs:
            return []

        counter_map = {}
        for s in strs:
            counter_map[s] = Counter(s)

        def isAnagram(s1: str, s2: str) -> bool:
            c1 = counter_map[s1]
            c2 = counter_map[s2]            

            for c, f in c1.items():
                if not (c in c2 and c2.get(c, -1) >= f):
                    return False
            
            for c, f in c2.items():
                if not (c in c1 and c1.get(c, -1) >= f):
                    return False

            return True

        remains = strs
        added = [False for i in range(len(strs))]
        rets = []
        for i in range(len(strs)):
            if added[i]:
                continue
            seed = strs[i]
            group = [seed]
            added[i] = True
            for j in range(i+1, len(strs)):
                if added[j]:
                    continue
                candidate = strs[j]
                if isAnagram(seed, candidate):
                    group.append(candidate)
                    added[j] = True

            rets.append(group)

        return rets

