class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        order = sorted(intervals, key=lambda x: x[0])
        counter = 0
        prev = None
        prevIndex = 0
        i = 0
        while i < len(order):
            item = order[i]
            print(prev, item)
            if prev and item[0] < prev[1]:
                if prev[1] > item[1]:
                    order.pop(prevIndex)
                    prev = item
                    prevIndex = i -1
                else:
                    order.pop(i)
                counter += 1        
            else:
                prev = item
                prevIndex = i
                i += 1
        return counter
            
        