class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = {}
        def dfs(index):
            if index >= len(nums) - 1:
                return index == len(nums) - 1
            if nums[index] == 0:
                return False
            if index in visited:
                return False
            
            for di in range(1, nums[index]+1):
                if dfs(index + di):
                    return True
                
            visited[index] = True
            return False
                

        return dfs(0)