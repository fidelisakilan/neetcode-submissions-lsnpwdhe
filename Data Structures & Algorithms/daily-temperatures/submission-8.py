class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                pi,pv = stack.pop()
                res[pi] = i - pi
            stack.append((i,v))
        return res



        