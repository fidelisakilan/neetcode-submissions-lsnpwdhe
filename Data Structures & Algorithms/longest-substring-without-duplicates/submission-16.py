class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l = 0
        r = 0
        bucket = set()
        res = 0
        while l <= r and r < len(s):
            while s[r] in bucket:
                bucket.remove(s[l])
                l += 1
            bucket.add(s[r])
            res = max(res, r-l+1)
            r += 1
        return res
