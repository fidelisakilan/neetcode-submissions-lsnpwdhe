class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        bucket = defaultdict(list)
        for a, b in prerequisites:
            bucket[a].append(b)
        visit = set()

        def dfs(index):
            if index in visit:
                return False
            if bucket[index] == []:
                return True
            visit.add(index)
            for pre in bucket[index]:
                if not dfs(pre):
                    return False
            visit.remove(index)
            bucket[index] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
