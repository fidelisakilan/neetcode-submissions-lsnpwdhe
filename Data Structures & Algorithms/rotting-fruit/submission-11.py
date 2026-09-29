class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    grid[i][j] = -999
                elif grid[i][j] == 1:
                    grid[i][j] = 999
                else:
                    grid[i][j] = 0

        visited = {}
        def dfs(i, j, time):
            if not (i in range(r) and j in range(c)):
                return
            if grid[i][j] == -999:
                return
            if (i,j) in visited and visited[(i,j)] < time:
                return
            visited[(i,j)] = time
            grid[i][j] = min(time, grid[i][j])
            dfs(i+1, j, time + 1)
            dfs(i-1, j, time + 1)
            dfs(i, j+1, time + 1)
            dfs(i, j-1, time + 1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    dfs(i,j, 0)
        res = 0
        for i in range(r):
            for j in range(c):
                print(grid[i])
                if grid[i][j] == 999:
                    return -1
                else: 
                    res = max(res, grid[i][j])
        return res