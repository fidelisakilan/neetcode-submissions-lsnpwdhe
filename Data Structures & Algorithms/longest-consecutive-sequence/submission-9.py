class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bucket = set(nums)
        res = 0
        for n in nums:
            streak = 0
            curr = n
            while curr - 1 not in bucket:
                while curr in bucket:
                    streak += 1
                    curr += 1
            res = max(res, streak)
        return res
        