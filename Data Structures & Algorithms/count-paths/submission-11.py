class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            if i not in range(0, m) or j not in range(0, n):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            res = 0
            if i < m:
                res = dfs(i+1, j)
            if j < n:
                res += dfs(i, j+1)
            memo[(i,j)] = res
            return res

        return dfs(0,0)