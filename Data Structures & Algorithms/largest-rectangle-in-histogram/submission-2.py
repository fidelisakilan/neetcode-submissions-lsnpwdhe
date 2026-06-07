class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [] # (i, h)
        for i in range(len(heights)):
            start_index = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                start_index = index
            stack.append((start_index, heights[i]))
        
        for i, h in stack:
            area = max(area, h * (len(heights) - i))
        return area
