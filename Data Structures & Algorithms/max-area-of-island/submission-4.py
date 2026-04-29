class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        visits = set()
        counter = 0
        
        def dfs(r, c):
            nonlocal visits, counter
            if r < 0 or c < 0 or r == rows or c == cols:
                return 
            if grid[r][c] == 0 or (r, c) in visits:
                return
            
            visits.add((r, c))
            counter += 1
            print(r, c)
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(rows):
            for j in range(cols):
                counter = 0
                dfs(i, j)
                maxArea = max(maxArea, counter)
        return maxArea