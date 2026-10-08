class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1: 
                    fresh_count += 1

        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                dirs = [(0,1), (0,-1), (1,0), (-1,0)]
                for di,dj in dirs:
                    ni,nj = i+di, j+dj
                    if ni in range(rows) and nj in range(cols) and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
                        fresh_count -= 1
            time += 1
        return time if fresh_count == 0 else -1


