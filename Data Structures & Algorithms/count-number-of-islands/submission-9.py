class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        # DFS
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
        
        # BFS
        def bfs(i, j):
            queue = deque([(i,j)])
            visited.add((i,j))
            while queue:
                i, j = queue.popleft()
                directions = [(-1,0), (1,0), (0, -1), (0,1)]
                for di, dj in directions:
                    r, c = i+di, j+dj
                    if r not in range(rows):
                        continue
                    if c not in range(cols):
                        continue
                    if not grid[r][c] == "1":
                        continue
                    if (r, c) in visited:
                        continue
                    queue.append((r, c))
                    visited.add((r,c))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j)
                    islands += 1

        

        return islands
