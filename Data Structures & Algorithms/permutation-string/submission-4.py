class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1)
        bucket = [0]*26
        bucket1 = [0]*26
        for i in range(len(s1)):
            bucket[ord(s1[i]) - ord('a')] += 1
            bucket1[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if bucket[i] == bucket1[i]: 
                matches += 1

        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            bucket1[index] += 1
            if bucket[index] == bucket1[index]:
                matches += 1
            elif bucket[index] + 1 == bucket1[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            bucket1[index] -= 1
            if bucket[index] == bucket1[index]:
                matches += 1
            elif bucket[index] - 1 == bucket1[index]:
                matches -= 1
            l += 1
        return matches == 26