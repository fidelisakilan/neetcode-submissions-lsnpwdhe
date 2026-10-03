class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # make sure that a -> b doesn't have b which was already visited by another item

        bucket = defaultdict(list)
        for e in edges:
            ea, eb = e
            bucket[ea].append(eb)
            bucket[eb].append(ea)

        visited = set()
        def dfs(i, prev):
            print(i, prev, visited)
            if i in visited:
                return False
            
            visited.add(i)
            for child in bucket[i]:
                if child == prev:
                    continue
                if not dfs(child, i):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n