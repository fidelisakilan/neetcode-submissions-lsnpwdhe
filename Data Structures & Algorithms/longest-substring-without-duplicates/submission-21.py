class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       l, r = 0,0
       bucket = set()
       res = 0
       while l <= r and r < len(s):
            # print(l, r)
            if s[r] not in bucket:
                # print(1)
                bucket.add(s[r])
                res = max(res, r - l + 1)
            else:
                # print(2)
                while s[r] in bucket:
                    bucket.remove(s[l])
                    l = l + 1
                bucket.add(s[r])
            r = r + 1
            # print(3)
       return res