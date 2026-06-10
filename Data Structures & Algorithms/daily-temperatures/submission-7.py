class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # maintain a stack for incomming elements
        # add a element in a empty stack
        # when incoming element is higher then remove the old value, 
        # but compute distance

        stack = []
        n = len(temperatures)
        res = [0]*n
        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                pi, _ = stack.pop()
                res[pi] = i - pi
            stack.append((i,v))
        return res
