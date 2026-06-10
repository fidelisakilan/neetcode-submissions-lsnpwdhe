class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = defaultdict(list)
        visited = set()

        for a, b in prerequisites:
            mapping[a].append(b)

        def dfs(n):
            if n in visited:
                return False
            
            if mapping[n] == []:
                return True
            
            visited.add(n)
            for pre in mapping[n]:
                if not dfs(pre): return False
            visited.remove(n)
            return True

            
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True