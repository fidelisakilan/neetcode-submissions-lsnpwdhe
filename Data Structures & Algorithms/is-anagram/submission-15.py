class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bucket = defaultdict(int)

        for i in range(len(s)):
            bucket[s[i]] += 1
            bucket[t[i]] -= 1
        
        for k, v in bucket.items():
            if v != 0:
                return False
        return True
