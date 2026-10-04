class Solution:
    def canJump(self, nums: List[int]) -> bool:
        found = False
        visited = set()
        def dfs(index):
            nonlocal found
            if found:
                return
            if index == len(nums) - 1: found = True
            if nums[index] == 0:
                return
            if index in visited:
                return

            visited.add(index)
            for di in range(1, nums[index] + 1):
                ni = index + di
                if ni in range(index, len(nums)):
                    dfs(ni)
                    if found: return
        dfs(0)
        print(visited)
        return found