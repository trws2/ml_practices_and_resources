# use heapq
# runtime: O(n + k x log(|unique_numbers|))
# space: O(|unique_numbers|)

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []
        for n, f in counter.items():
            heapq.heappush(heap, (-f, n))
        
        ret = []
        while len(ret) < k:
            n = heapq.heappop(heap)[1]
            ret.append(n)

        return ret

# use sorted function
# runtime: O(n + |unique_numbers| x log(|unique_numbers|))
# space: O(|unique_numbers|)

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freqs = [(n, f) for n, f in counter.items()]
        freqs = sorted(freqs, key=lambda x : x[1], reverse=True)
        freqs = freqs[:k]
        return [x[0] for x in freqs]



