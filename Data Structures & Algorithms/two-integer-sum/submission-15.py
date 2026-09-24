class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        for i, n in enumerate(nums):
            if n not in bucket:
                bucket[target - n] = i
            else:
                return [bucket[n], i]