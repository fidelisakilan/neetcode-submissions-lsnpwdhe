class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_set = {}
        max_len = 0
        l, r = 0,0
        while r < len(s):
            if s[r] not in unique_set:
                print( l, r, s[l:r+1])
                unique_set[s[r]] = r
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                l = unique_set[s[r]] + 1
                r = l
                unique_set = {}
        return max_len
