class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for i in count:
            if i != 0:
                return False
        return True




        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i],0) + 1
            dict2[t[i]] = dict2.get(t[i],0) + 1

        for k,v in dict1.items():
            if k not in dict2 or dict2[k] != v:
                return False
        print(dict1, dict2)
        return True