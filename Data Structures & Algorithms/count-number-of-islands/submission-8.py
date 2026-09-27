class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(i, j):
            if i not in range(rows):
                return
            if j not in range(cols):
                return
            if not grid[i][j] == "1":
                return
            if (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

                


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    islands += 1

        return islands
