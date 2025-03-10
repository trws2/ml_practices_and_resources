# runtime: O(n)
# space: O(n)

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
