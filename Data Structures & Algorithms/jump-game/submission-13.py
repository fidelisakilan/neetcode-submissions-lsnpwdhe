class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(index):
            if index in memo:
                return memo[index]
            if index >= len(nums) - 1:
                return index == len(nums) - 1
            for j in range(index+1, index + nums[index] + 1):
                if dfs(j): 
                    memo[index] = True
                    return True
                memo[index] = False
            return False
        return dfs(0)