class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        depth = 0
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        while (l <= r):
            if maxL < maxR:
                depth += max(maxL - height[l], 0)
                maxL = max(maxL, height[l])
                l += 1
            else:
                depth += max(maxR - height[r], 0)
                maxR = max(maxR, height[r])
                r -= 1
        return depth
            

                
