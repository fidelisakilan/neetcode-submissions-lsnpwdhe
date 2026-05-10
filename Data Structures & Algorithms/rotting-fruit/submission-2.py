class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c, level):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == -1 or grid[r][c] < level:
                return
            
            grid[r][c] = level
            dfs(r+1, c, level+1)
            dfs(r-1, c, level+1)
            dfs(r, c+1, level+1)
            dfs(r, c-1, level+1)

        for i in range(rows):
            for j in range(cols):
                element = grid[i][j]
                if element == 0:
                    grid[i][j] = -1
                elif element == 1:
                    grid[i][j] = 2147483647
                elif element == 2:
                    grid[i][j] = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    print("Hello")
                    dfs(i, j, 0)
    
        minutes = 0
        for i in range(rows):
            for j in range(cols):
                print(grid[i][j], end=" ")
            print()
        
        for i in range(rows):
            for j in range(cols):
                element = grid[i][j] 
                if element == 2147483647:
                    return -1
                else:
                    minutes = max(minutes, grid[i][j])
        return minutes
        