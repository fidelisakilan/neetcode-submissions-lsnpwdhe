class Node:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visitSet = set()
        

        for (a,b) in prerequisites:
            preMap[a].append(b)
        
        def dfs(n):
            if n in visitSet:
                return False
            if preMap[n] == []:
                return True

            visitSet.add(n)
            for child in preMap[n]:
                if not dfs(child): return False
            visitSet.remove(n)
            return True
        
        for n in range(numCourses):
            if not dfs(n): return False
        return True
        
        
        


        