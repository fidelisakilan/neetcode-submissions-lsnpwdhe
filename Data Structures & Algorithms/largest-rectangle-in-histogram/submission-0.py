class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (i,h)
        area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                start = index
            stack.append((start, heights[i]))
        
        for i, h in stack:
            area = max(area, h * (len(heights) - i))
        return area

