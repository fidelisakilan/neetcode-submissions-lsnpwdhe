class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        length = len(s)
        
        dict_letters = {}

        for i in range(length):
            if s[i] not in dict_letters:
                dict_letters[s[i]] = 0
            if t[i] not in dict_letters:
                dict_letters[t[i]] = 0
            dict_letters[s[i]] = dict_letters[s[i]] - 1 
            dict_letters[t[i]] = dict_letters[t[i]] + 1 
        for i in dict_letters.values():
            if i != 0:
                return False
        return True