class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1) - 1
        bucket = [0]*26
        bucket1 = [0]*26
        for letter in s1:
            bucket[ord(letter) - ord('a')] += 1
        for letter in s2[0:len(s1)]:
            bucket1[ord(letter) - ord('a')] += 1

        while r < len(s2):
            if bucket == bucket1:
                return True
            r += 1
            if r < len(s2):
                bucket1[ord(s2[r]) - ord('a')] += 1

            bucket1[ord(s2[l]) - ord('a')] -= 1
            l += 1
        return False