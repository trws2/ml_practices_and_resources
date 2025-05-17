class HitCounter:

    def __init__(self):
        self.hits = []
        self.valid_range = 299
        
    def hit(self, timestamp: int) -> None:
        start = timestamp
        end = timestamp + self.valid_range
        self.hits.append([start, end])

    def getHits(self, timestamp: int) -> int:
        res = 0
        for i in range(len(self.hits)-1, -1, -1):
            start, end = self.hits[i]
            if timestamp > end:
                break
            res += 1
        return res
        
