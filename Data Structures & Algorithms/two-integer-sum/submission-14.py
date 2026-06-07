class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        for i, n in enumerate(nums):
            if (target-n) in bucket:
                return [bucket[target-n], i]
            bucket[n] = i
        return [0,0]