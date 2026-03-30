class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_bucket = {}

        for i, n in enumerate(nums):
            if n in diff_bucket:
                return [diff_bucket[n], i]
            diff_bucket[target - n] = i
        return None