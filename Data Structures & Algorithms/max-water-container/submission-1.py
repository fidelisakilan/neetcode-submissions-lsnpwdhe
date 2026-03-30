class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_container = 0
        while (l < r): 
            container_size = (r - l) * min(heights[l], heights[r])
            max_container = max(container_size, max_container)
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return max_container