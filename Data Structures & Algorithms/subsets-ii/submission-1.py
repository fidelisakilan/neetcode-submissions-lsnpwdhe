class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        seq = []
        nums.sort()
        def backtrack(index):
            if index == len(nums):
                result.append(seq[::])
                return
            seq.append(nums[index])
            backtrack(index+1)
            seq.pop()
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index+1)
        backtrack(0)
        return result
        