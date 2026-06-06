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
        sorted_meetings = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if not sorted_meetings[i].start >= sorted_meetings[i-1].end:
                return False
        return True
