class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ordered = sorted(intervals, key=lambda x: x[0])
        data = []

        for item in ordered:
            s, e = item
            if not data:
                data.append([s,e])
            elif s <= data[-1][1]:
                popped = data.pop()
                data.append([popped[0], max(popped[1], e)])
            else:
                data.append([s,e])
        return data
                
            
        