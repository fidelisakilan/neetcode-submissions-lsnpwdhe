class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j, dist, visited):
            if i < 0 or j < 0 or i == rows or j == cols or grid[i][j] < dist:
                return
            # visited.add((i,j))
            print(dist, grid[i][j])
            grid[i][j] = min(dist, grid[i][j])
            dfs(i+1, j, dist+1, visited)
            dfs(i, j+1, dist+1, visited)
            dfs(i-1, j, dist+1, visited)
            dfs(i, j-1, dist+1, visited)
        
        for r in range(rows):
            for l in range(cols):
                if grid[r][l] == 0:
                    dfs(r, l, 0, set())

                
                

        

        