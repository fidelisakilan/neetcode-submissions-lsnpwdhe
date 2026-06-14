class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        items = []
        def backtrack(index, total):
            if total == target:
                res.append(items.copy())
                return
            
            if index >= len(nums) or total > target :
                return

            items.append(nums[index])
            backtrack(index, total + nums[index])
            items.pop()
            backtrack(index+1, total)
            
        
        backtrack(0, 0)
        return res