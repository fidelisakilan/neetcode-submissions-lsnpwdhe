class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        s, e = newInterval
        while i < len(intervals) and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        res.append([s,e])
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res