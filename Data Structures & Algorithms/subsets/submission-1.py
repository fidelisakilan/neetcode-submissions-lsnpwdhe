class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        seq = []

        def dfs(index):
            if index >= len(nums):
                result.append(seq.copy())
                return
            
            seq.append(nums[index])
            dfs(index+1)

            seq.pop()
            dfs(index+1)

            
        
        dfs(0)
        return result
        