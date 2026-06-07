class Solution:
    def maxArea(self, heights: List[int]) -> int:
        target_max = 0
        l, r = 0, len(heights) - 1
        while l < r:
            target = min(heights[l], heights[r])*(r-l)
            print(l, r, target)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            target_max = max(target_max, target)
        return target_max 