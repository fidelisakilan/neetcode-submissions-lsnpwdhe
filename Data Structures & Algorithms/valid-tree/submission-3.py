class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        links = defaultdict(list)
        visits = set()
        for n1,n2 in edges:
            links[n1].append(n2)
            links[n2].append(n1)

        def dfs(i, prev):
            if i in visits:
                return False
            visits.add(i)
            for link in links[i]:
                if prev == link:
                    continue
                if not dfs(link, i):
                    return False
            return True
        
        return dfs(0, -1) and len(visits) == n
        

