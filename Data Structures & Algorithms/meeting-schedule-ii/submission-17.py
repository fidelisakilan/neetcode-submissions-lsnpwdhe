"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        # keep track of end of incoming rooms
        # check if incoming date start < end of old
        # if yes, incoming needs a new room with its own end date
        # if not, update the current room end date
        # but first lets sort the incoming dates
        intervals.sort(key = lambda x: x.start)

        heap = []
        heapq.heappush(heap, intervals[0].end)
        
        for i in intervals[1:]:
            s, e = i.start, i.end
            if s < heap[0]:
                heapq.heappush(heap, e)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, e)
        
        return len(heap)
            
            



        