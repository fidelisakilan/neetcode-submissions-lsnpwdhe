class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 0  or 1
        # if 0 then pay for 0 then branch 2 paths, either 0 + 1 or 0 + 2
        # 0 
        # 1 | 2
        # (2, 3) | (3, 4)
        memo = {}
        def dfs(i):
            if i == len(cost):
                return 0
            if i > len(cost):
                return float("inf")
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]
        
        return min(dfs(0), dfs(1))
            

