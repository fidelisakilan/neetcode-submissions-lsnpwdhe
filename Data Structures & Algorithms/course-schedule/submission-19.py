class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)

        for a, b in prerequisites:
            prereq[a].append(b)
        visited = set()
        print(prereq)
        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            for child in prereq[i]:
                if not dfs(child):
                    return False
            visited.remove(i)
            prereq[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        