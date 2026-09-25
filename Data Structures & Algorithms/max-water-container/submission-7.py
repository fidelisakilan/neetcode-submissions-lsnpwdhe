class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        product = 0
        while l < r:
            product = max(product, min(heights[l], heights[r]) * (r-l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return product

