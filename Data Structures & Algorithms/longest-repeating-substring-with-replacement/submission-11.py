class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l = 0
        r = 0
        res = 0
        while l <= r and r < len(s):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            while (r - l + 1) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
            r += 1
        return res