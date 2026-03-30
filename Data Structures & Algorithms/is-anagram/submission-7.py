class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table = [0 for _ in range(26)]
        for i in range(0, len(s)):
            hash_table[ord(s[i]) - ord('a')] += 1
            hash_table[ord(t[i]) - ord('a')] -= 1
        for count in hash_table:
            if count != 0:
                return False
        return True
