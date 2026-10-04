class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        def dfs(index):
            if index == len(cost):
                return 0
            if index > len(cost):
                return float("inf")            
            if memo[index] != -1:
                return memo[index]

            memo[index] = cost[index] + min(dfs(index+1), dfs(index+2))
            return memo[index]
        return min(dfs(0), dfs(1))
        