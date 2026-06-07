class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        i = 0
        res = []
        while i < len(intervals) and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= e:
            s = min(intervals[i][0], s)
            e = max(intervals[i][1], e)
            i += 1
        res.append([s,e])
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res