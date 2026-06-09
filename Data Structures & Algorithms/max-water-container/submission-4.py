class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        amt = 0

        while l <= r:
            side = min(heights[l], heights[r])
            rect = side * (r - l)
            print(side)
            amt = max(amt, rect)
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return amt