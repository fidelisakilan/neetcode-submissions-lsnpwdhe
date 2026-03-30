class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bucket = {}
        for n in nums:
            if n in bucket:
                return True
            bucket[n] = 1
        return False