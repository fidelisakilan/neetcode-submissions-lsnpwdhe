class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        pres, ares = set(), set()
        visited = set()

        def dfs(i, j, visit, prevHeight):
            if not (i in range(r) and j in range(c)):
                return
            if (i,j) in visit:
                return
            if heights[i][j] < prevHeight:
                return

            visit.add((i,j))
            dfs(i+1,j, visit, heights[i][j])
            dfs(i-1,j, visit, heights[i][j])
            dfs(i,j+1, visit, heights[i][j])
            dfs(i,j-1, visit, heights[i][j])


        for i in range(c):
            # pacific top
            dfs(0, i, pres, 0)
            # atlantic bottom
            dfs(r-1, i, ares, 0)
        
        for i in range(r):
            # pacific left
            dfs(i, 0, pres, 0)
            # atlantic right
            dfs(i, c-1, ares, 0)

        res = []
        print(pres, ares)
        for i in range(r):
            for j in range(c):
                if (i,j) in ares and (i,j) in pres:
                    res.append([i,j])
        return res




