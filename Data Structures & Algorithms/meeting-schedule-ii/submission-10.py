"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)
        data = []
        heapq.heapify(data)
        sorted_meetings = sorted(intervals, key=lambda x: x.start)
        heapq.heappush(data, sorted_meetings[0].end)
        for i in range(1, len(sorted_meetings)):
            if sorted_meetings[i].start >= data[0]:
                heapq.heappop(data)
                heapq.heappush(data, sorted_meetings[i].end)
            else:
                heapq.heappush(data, sorted_meetings[i].end)
        return len(data)