class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        prevEnd = None
        counter = 0
        intervals.sort()
        for i in range(len(intervals)):
            if prevEnd and intervals[i][0] < prevEnd:
                prevEnd = min(prevEnd, intervals[i][1])
                counter += 1
            else:
                prevEnd = intervals[i][1]
        return counter
        