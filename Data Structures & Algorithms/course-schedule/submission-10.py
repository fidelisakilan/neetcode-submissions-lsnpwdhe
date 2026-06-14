class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for a, b in prerequisites:
            prereq[a].append(b)
        
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if prereq[course] == []:
                return True
            
            visit.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
