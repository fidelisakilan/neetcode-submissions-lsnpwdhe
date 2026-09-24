class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bucket = set()
        for n in nums:
            if n not in bucket:
                bucket.add(n)
                continue
            return True
        return False
        