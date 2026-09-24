class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        bucket1 = defaultdict(int)
        bucket2 = defaultdict(int)

        for i in range(len(s)):
            bucket1[s[i]] += 1
            bucket2[t[i]] += 1
        
        return bucket1 == bucket2