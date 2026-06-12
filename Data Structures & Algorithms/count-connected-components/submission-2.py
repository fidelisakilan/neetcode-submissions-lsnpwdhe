class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapping = defaultdict(set)
        for a,b in edges:
            mapping[a].add(b)
            mapping[b].add(a)
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            if node in data:
                data.remove(node)
            for nei in mapping[node]:
                dfs(nei)
        count = 0
        data = set([ int(i) for i in range(n)])
        
        while data:
            popped = data.pop()
            count += 1
            dfs(popped)
            print(popped, data)
        return count

            
