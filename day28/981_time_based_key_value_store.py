class TimeMap:

    def __init__(self):
        self.dic = {}

    # runtime: O(1)
    # space: O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.dic:
            self.dic[key] = []
        self.dic[key].append((value, timestamp))

    # runtime: O(log(n))
    # space: O(n)
    def get(self, key: str, timestamp: int) -> str:
        values = self.dic.get(key, [])
        if not values:
            return ""

        left, right = 0, len(values)-1
        while left < right:
            mid = int((left + right) / 2)
            v, t = values[mid][0], values[mid][1]
            if t == timestamp:
                return v

            if t < timestamp:
                left = mid + 1
                continue

            right = mid

        if timestamp >= values[left][1]:
            return values[left][0]
        
        if left == 0:
            return ""

        return values[left-1][0]

# the following solutio based linear search in reverse order is actually faster
#
# class TimeMap:

#     def __init__(self):
#         self.dic = {}

#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.dic:
#             self.dic[key] = []
#         self.dic[key].append([value , timestamp])

#     def get(self, key: str, timestamp: int) -> str:
#         res = ""
#         values = self.dic.get(key , [])
#         if not values:
#             return ""

#         for i in range(len(values)-1, -1, -1):
#             v = values[i][0]
#             t = values[i][1]
#             if t <= timestamp:
#                 return v

#         return ""









# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)












