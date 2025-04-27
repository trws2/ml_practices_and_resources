# runtime: O(n)
# space: O(n)

# the following solution is more clear. Note that we do not do append anything in the 3rd condition in the for loop
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                ret.append(interval)
            elif newInterval[1] < interval[0]:
                ret.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        
        ret.append(newInterval)
        return ret


# the following solutio works, but the codig looks complicated.
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(inter1, inter2):
            if inter1[1] < inter2[0] or inter2[1] < inter1[0]:
                return False
            return True

        if not intervals:
            return [newInterval]
        
        if newInterval[1] < intervals[0][0]:
            ret = [newInterval]
            ret.extend(intervals)
            return ret

        ret = []
        new_interval_added = False
        for interval in intervals:
            if new_interval_added == False:
                if overlap(interval, newInterval):
                    new_start = min(newInterval[0], interval[0])
                    new_end = max(newInterval[1], interval[1])
                    ret.append([new_start, new_end])
                    new_interval_added = True
                else:
                    if interval[1] < newInterval[0]:
                        ret.append(interval)
                    else:
                        ret.append(newInterval)
                        ret.append(interval)
                        new_interval_added = True
            else:
                if overlap(interval, ret[-1]):
                    new_start = min(ret[-1][0], interval[0])
                    new_end = max(ret[-1][1], interval[1])
                    ret[-1] = [new_start, new_end]
                else:
                    ret.append(interval)

        if not new_interval_added:
            ret.append(newInterval)

        return ret



