class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        seq = []

        def backtrack(index, total):
            if index >= len(nums) or total > target:
                return
            if total == target:
                result.append(seq[::])
                return
            seq.append(nums[index])
            backtrack(index, total + nums[index])
            seq.pop()
            backtrack(index+1, total)
        backtrack(0,0)
        return result