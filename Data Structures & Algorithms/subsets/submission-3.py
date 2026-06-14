class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        content = []

        def dfs(i):
            if i == len(nums):
                res.append(content.copy())
                return
            
            content.append(nums[i])
            dfs(i+1)
            content.pop()
            dfs(i+1)
        
        dfs(0)
        return res