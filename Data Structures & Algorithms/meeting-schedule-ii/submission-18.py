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
        intervals.sort(key= lambda x: x.start)
        rooms = [intervals[0].end]
        heapq.heapify(rooms)
        for interval in intervals[1:]:
            if interval.start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval.end)
        return len(rooms)
            

            
