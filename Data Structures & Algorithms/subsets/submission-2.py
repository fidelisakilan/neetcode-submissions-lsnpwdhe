class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        seq = []
        def backtrack(index):
            if index == len(nums):
                result.append(seq[::])
                return
            seq.append(nums[index])
            backtrack(index+1)
            seq.pop()
            backtrack(index+1)
        backtrack(0)
        return result
        