class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_dict = {}
        for i in s:
            count_dict[i] = count_dict.get(i, 0) + 1
        print(count_dict)
        for i in t:
            if i not in count_dict:
                return False
            if count_dict[i] == 1:
                count_dict.pop(i)
            else:
                count_dict[i] = count_dict[i] - 1

        return count_dict == {}
        