class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        res = []
        for a, b in prerequisites:
            prereq[a].append(b)

        visited = set()
        skip = set()
        def dfs(i):
            if i in skip:
                return True
            if i in visited:
                return False
            if prereq[i] == []:
                res.append(i)
                skip.add(i)
                return True
            
            visited.add(i)
            for p in prereq[i]:
                if not dfs(p):
                    return False
            visited.remove(i)
            res.append(i)
            skip.add(i)
            return True

        for i in range(numCourses):
            if not dfs(i) and i not in skip:
                return []
        print(res)
        return res