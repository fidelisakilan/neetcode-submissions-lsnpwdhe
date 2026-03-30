class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # First find if missing number is present in dict
        # if yes then return the index of target and current
        # else store the target to dict
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i