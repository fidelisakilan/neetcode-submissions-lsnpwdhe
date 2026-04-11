class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        seq = []
        def dfs(index, total):
            if total == target:
                result.append(seq.copy())
                return
            if total > target or index >= len(nums):
                return

            seq.append(nums[index])
            dfs(index, total + nums[index])
            seq.pop()
            dfs(index+1, total)
        dfs(0,0)
        return result
        