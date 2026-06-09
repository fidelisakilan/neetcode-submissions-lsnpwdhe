class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bucket = set()

        l = 0
        r = 0
        res = 0
        while l <= r and r < len(s):
            while s[r] in bucket:
                bucket.remove(s[l])
                l += 1
            bucket.add(s[r])
            res = max(res, len(bucket))
            r += 1
        return res
        