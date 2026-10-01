class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bucket = set(nums)
        res = 0
        for i, n in enumerate(nums):
            curr = n
            if (n - 1) not in bucket:
                while curr in bucket :
                    curr += 1
                res = max(res, curr - n)
        return res