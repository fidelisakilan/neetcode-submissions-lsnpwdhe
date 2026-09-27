"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True
        intervals.sort(key= lambda x: x.start)
        prevEnd = intervals[0].end
        for i in intervals[1:]:
            s, e = i.start, i.end
            if s < prevEnd:
                return False
            else:
                prevEnd = e
        return True