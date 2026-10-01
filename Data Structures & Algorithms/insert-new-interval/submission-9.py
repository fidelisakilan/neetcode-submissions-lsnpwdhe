class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        

        # my approach woudl be
        # first add all intervals with end < ni.start to res
        # if end of curr is greater than ni.start then iterate  untitl you find a end greater than ni.start.. 
        # add that new range element and  
        # add the remaining list from the og

        i = 0
        l = len(intervals)
        s, e = newInterval
        res = []
        while i < l and intervals[i][1] < s:
            res.append(intervals[i])
            i += 1
        while i < l and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        res.append([s,e])
        while i < l:
            res.append(intervals[i])
            i += 1
        return res

