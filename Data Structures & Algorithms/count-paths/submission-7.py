class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i, j):
            if not (i in range(m) and j in range(n)):
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            res = dfs(i, j + 1) + dfs(i+1, j)
            memo[(i,j)] = res
            return res

        return dfs(0, 0)