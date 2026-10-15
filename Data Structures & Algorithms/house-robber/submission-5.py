class Solution:
    def rob(self, nums: List[int]) -> int:
        memo =  {}
        def dfs(index):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            memo[index] = max(nums[index] + dfs(index+2), dfs(index+1))
            return memo[index]
        return dfs(0)