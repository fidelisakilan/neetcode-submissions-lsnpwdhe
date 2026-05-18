class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.counter = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c, following):
            if r < 0 or c < 0 or r == rows or c == cols:
                return
            if grid[r][c] == "0" or grid[r][c] == "#":
                return
            
            grid[r][c] = "#"
            if not following:
                self.counter += 1
            dfs(r+1, c, True)
            dfs(r-1, c, True)
            dfs(r, c+1, True)
            dfs(r, c-1, True)
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, False)
        return self.counter
        