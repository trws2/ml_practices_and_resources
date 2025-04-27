class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        # scan intervals to find the first interval to insert the start point and 
        # update the newInterval start and end points based oon the inserting interval
        ret = []
        newInterval_added = False
        for interval in intervals:
            # non-overlapping case
            if interval[1] < newInterval[0]:
                ret.append(interval)
                continue
            
            if newInterval[1] < interval[0]:
                if not newInterval_added:
                    ret.append(newInterval)
                    newInterval_added = True
                ret.append(interval)
                continue

            # overlapping case
            new_start = min(interval[0], newInterval[0])
            new_end = max(interval[1], newInterval[1])
            newInterval = [new_start, new_end]            
            if not newInterval_added:
                ret.append(newInterval)
            else:
                ret[-1] = newInterval
            newInterval_added = True

        if not newInterval_added:
            ret.append(newInterval)

        return ret

