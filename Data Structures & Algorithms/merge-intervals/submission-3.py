class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        data = []
        for i in range(len(intervals)):
            s, e = intervals[i]
            if len(data) and s <= data[-1][1]:
                popped = data.pop()
                data.append([min(popped[0], s), max(popped[1], e)])
            else:
                data.append(intervals[i])
        return data