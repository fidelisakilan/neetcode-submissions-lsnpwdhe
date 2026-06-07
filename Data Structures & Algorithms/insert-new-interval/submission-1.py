class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        bucket = []
        i = 0
        s, e = newInterval
        length = len(intervals)
        while i < length and intervals[i][1] < s:
            bucket.append(intervals[i])
            i += 1
        print(bucket)
        newStart = s
        newEnd = e

        while i < length and newEnd >= intervals[i][0]:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1
        bucket.append([newStart, newEnd])
        while i < length:
            bucket.append(intervals[i])
            i += 1
        return bucket

