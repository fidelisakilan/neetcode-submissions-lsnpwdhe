class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = defaultdict(list)
        visited = set()
        order = []
        output_set = set()

        for (k,v) in prerequisites:
            premap[k].append(v)
        
        def dfs(n):
            if n in visited: 
                return False
            if premap[n] == []:
                if n not in output_set:
                    order.append(n)
                    output_set.add(n)
                return True
            
            visited.add(n)
            for r in premap[n]:
                if not dfs(r): return False
            visited.remove(n)
            if n not in output_set:
                order.append(n)
                output_set.add(n)
            premap[n] = []
            return True
        

        for n in range(numCourses):
            if not dfs(n):
                return []
        return list(order)

