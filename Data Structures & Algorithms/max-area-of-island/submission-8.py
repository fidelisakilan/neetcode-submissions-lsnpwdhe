class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j, visited):
            if i < 0 or j < 0 or i == rows or j == cols or grid[i][j] == 0:
                return
            grid[i][j] = 0
            visited.add((i, j))
            dfs(i+1, j, visited)
            dfs(i-1, j, visited)
            dfs(i, j+1, visited)
            dfs(i, j-1, visited)

        counter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    visited = set()
                    dfs(i, j, visited)
                    counter = max(counter, len(visited))
        return counter 
        