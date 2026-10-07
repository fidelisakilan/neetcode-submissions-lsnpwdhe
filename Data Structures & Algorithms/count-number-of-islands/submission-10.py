class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):
            if not (i in range(rows) and j in range(cols)):
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = "0"
            dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in dirs:
                dfs(i+di, j+dj)
        
        
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        return islands

