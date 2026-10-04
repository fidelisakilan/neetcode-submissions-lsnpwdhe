class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combination = []
        res = []
        def backtrack(i, total):
            if total == target:
                res.append(combination.copy())
                return
            if total > target:
                return
            if i not in range(len(nums)):
                return

            combination.append(nums[i])
            backtrack(i, total+nums[i])
            combination.pop()
            backtrack(i+1, total)
        
        backtrack(0, 0)
        return res


