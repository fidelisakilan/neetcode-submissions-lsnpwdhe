class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []
        i = 0
        while i < n:
            # remove less values from the stack and store result
            while stack and stack[-1][0] < temperatures[i]:
                pval, pi = stack.pop()
                res[pi] = i - pi
            stack.append([temperatures[i], i])
            i += 1
        return res