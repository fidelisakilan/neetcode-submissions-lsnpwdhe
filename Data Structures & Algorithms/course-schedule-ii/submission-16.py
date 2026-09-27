class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for c,p in prerequisites:
            prereq[c].append(p)
        
        visited = set()
        skip = set()
        order = []

        def dfs(course):
            if course in visited:
                return False
            if course in skip:
                return True

            visited.add(course)
            for p in prereq[course]:
                res = dfs(p)
                if not res: return False
            visited.remove(course)
            prereq[course] = []
            order.append(course)
            skip.add(course)
            return True
        for i in range(numCourses):
            res = dfs(i)
            if not res: return []
        return order

