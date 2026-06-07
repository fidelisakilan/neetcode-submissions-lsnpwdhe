"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        bookings = []
        heapq.heapify(bookings)
        intervals.sort(key=lambda x: x.start)
        i = 0
        while i < len(intervals):
            if bookings and intervals[i].start >= bookings[0]:
                heapq.heappop(bookings)
                heapq.heappush(bookings, intervals[i].end)
            else:
                heapq.heappush(bookings, intervals[i].end)
            i += 1
        return len(bookings)
                    
