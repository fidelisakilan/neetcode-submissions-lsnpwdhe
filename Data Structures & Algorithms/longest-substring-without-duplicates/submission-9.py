class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # unique_set = {}
        # max_len = 0
        # l, r = 0,0
        # while r < len(s):
        #     if s[r] not in unique_set:
        #         print( l, r, s[l:r+1])
        #         unique_set[s[r]] = r
        #         max_len = max(max_len, r - l + 1)
        #         r += 1
        #     else:
        #         l = unique_set[s[r]] + 1
        #         r = l
        #         unique_set = {}
        # return max_len
        
        char_set = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res

        # mp = {} # dictionary with index of each character
        # res = 0
        # l = 0
        # for r in range(len(s)): # iterate through each char in string
        #     if s[r] in mp: # if char is already present in substring
        #         l = max(mp[s[r]]+1, l) # make the starting element to be first 
        #     mp[s[r]] = r
        #     res = max(res, r - l + 1)
        # return res
