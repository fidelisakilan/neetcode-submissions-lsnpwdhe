class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table = [0] * 26

        for i in range(len(s)):
            hash_table[ord(s[i]) - ord('a')] += 1
            hash_table[ord(t[i]) - ord('a')] -= 1
        
        for count in hash_table:
            if count != 0:
                return False
        print(hash_table)
        return True

        