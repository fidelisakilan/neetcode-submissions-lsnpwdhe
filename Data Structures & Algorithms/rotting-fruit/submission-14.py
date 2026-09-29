class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        queue = deque()
        visited = set()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    visited.add((i, j))
                    queue.append((i,j))
            
        time = 0
        print(visited)
        while queue:
            length = len(queue)
            print(queue)
            for _ in range(length):
                i, j = queue.popleft()
                directions = [[-1,0], [1,0], [0,-1], [0,1]]
                for dir in directions:
                    di, dj = dir
                    ni, nj = i + di, j + dj
                    if ni in range(r) and nj in range(c) and grid[ni][nj] == 1 and (ni,nj) not in visited:
                        queue.append((ni,nj))
                        visited.add((ni,nj))

            time += 1
        print(visited)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (i,j) not in visited:
                    print(i,j)
                    return -1
        if visited:
            return time - 1
        else: return 0

