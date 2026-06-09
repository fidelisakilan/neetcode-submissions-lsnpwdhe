class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0]*n
        rightMax = [0]*n
        
        for i in range(n):
            if i == 0:
                leftMax[0] = height[0]
            else:
                leftMax[i] = max(leftMax[i-1], height[i])
        
        for i in range(n-1, -1, -1):
            if i == n-1:
                rightMax[n-1] = height[n-1]
            else:
                rightMax[i] = max(rightMax[i+1], height[i])
        
        print(leftMax, rightMax)
        trapped = 0
        for i in range(n):
            val = min(leftMax[i], rightMax[i]) - height[i]
            print(val)
            if val > 0:
                trapped += val
            
        return trapped
        