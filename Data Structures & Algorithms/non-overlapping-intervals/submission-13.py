class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        lastEnd = intervals[0][1]
        counter = 0
        for s, e in intervals[1:]:
            if s < lastEnd:
                lastEnd = min(e, lastEnd)
                counter += 1
                print(s, e, lastEnd)
            else:
                lastEnd = e
        return counter
        