class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        seq = []
        length = len(nums)
        def dfs(index, total):
            if total == target:
                output.append(seq.copy())
                return
            if index >= length or total > target:
                return
            
            seq.append(nums[index])
            dfs(index, total + nums[index])
            seq.pop()
            dfs(index+1, total)
        
        dfs(0, 0)
        return output

        