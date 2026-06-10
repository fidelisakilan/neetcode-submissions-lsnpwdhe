class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = []
        
        for i in range(len(heights)):
            if not stack:
                stack.append((i, heights[i]))
            starting = i
            while stack and heights[i] < stack[-1][1]:
                pi, pv = stack.pop()
                rect = (i - pi) * pv
                maxArea = max(maxArea, rect)
                starting = pi
            stack.append((starting, heights[i]))
        
        for i, v in stack:
            rect = (len(heights) - i) * v
            maxArea = max(maxArea, rect)
        return maxArea