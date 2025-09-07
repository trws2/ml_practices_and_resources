# newer
class UnionFind():
    def __init__(self):
        self.parent = {}

    def union(self, x: str, y: str) -> None:
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[px] = py

    def find(self, x: str) -> bool:
        parent = self.parent.get(x, "")
        if parent == "":
            self.parent[x] = x
            return x
        if parent == x:
            return x
        return self.find(parent)


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        uf = UnionFind()

        if len(sentence1) != len(sentence2):
            return False

        for pair in similarPairs:
            uf.union(pair[0], pair[1])

        for w1, w2 in zip(sentence1, sentence2):
            r1 = uf.find(w1)
            r2 = uf.find(w2)
            if r1 != r2:
                return False

        return True



# older

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        parents = defaultdict()

        def find(x):
            if x not in parents:
                parents[x] = x
                return x
            if x == parents[x]:
                return x
            return find(parents[x])

        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                parents[px] = py

        for w1, w2 in similarPairs:
            union(w1, w2)

        for w1, w2 in zip(sentence1, sentence2):
            p1 = find(w1)
            p2 = find(w2)
            if p1 != p2:
                return False
        return True

