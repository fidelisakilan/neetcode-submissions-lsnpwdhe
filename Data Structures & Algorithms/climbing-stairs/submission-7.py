class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n
        def dfs(index):
            if index == n:
                return 1
            if index > n:
                return 0
            if memo[index] != -1:
                return memo[index] 
            memo[index] = dfs(index+1) + dfs(index+2)
            return memo[index]
        return dfs(0)
