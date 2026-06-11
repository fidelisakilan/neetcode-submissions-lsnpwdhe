class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        counter = defaultdict(int)
        res = 0

        while l <= r and r < len(s):
            counter[s[r]] += 1
            print(s[l:r+1])
            while counter and (r - l +1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res