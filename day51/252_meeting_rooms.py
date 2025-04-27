# runtime: O(n)
# space: O(1)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: (x.start, x.end))

        last_interval = None
        for interval in intervals:
            if not last_interval:
                last_interval = interval
            elif last_interval.end <= interval.start:
                last_interval = interval
            else:
                return False
        
        return True



