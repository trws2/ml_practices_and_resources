# runtime: O(n x log(n)), where n is number of intervals
# space: O(|result_list|) = O(n)

# new implementation that is shorter
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x : (x[0], x[1]))
        ret = []
        for interval in intervals:
            if not ret:
                ret.append(interval)            
            if ret[-1][1] < interval[0]:
                ret.append(interval)
            elif interval[0] <= ret[-1][1]:
                ret[-1][0] = min(ret[-1][0], interval[0])
                ret[-1][1] = max(ret[-1][1], interval[1])

        return ret


# older implementation
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals and len(intervals) == 1:
            return intervals

        # sort intervals by starting point
        sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        prev_start = -1
        prev_end = -1

        res = []
        for inter in sorted_intervals:
            start = inter[0]
            end = inter[1]

            if prev_start == -1 and prev_end == -1:
                res.append(inter)
            elif prev_end < start:
                # not overlap with previous interval                
                res.append(inter)
            else:
                # overlap with previous interval
                new_start = min(prev_start, start)
                new_end = max(prev_end, end)
                res[-1][0] = new_start
                res[-1][1] = new_end

            prev_start = res[-1][0]
            prev_end = res[-1][1]               

        return res
