class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        b1 = [0]*26
        b2 = [0]*26

        for s in s1:
            b1[ord(s) - ord("a")] += 1
        
        while r < len(s2):            
            while (r - l + 1) > len(s1):
                b2[ord(s2[l]) - ord("a")] -= 1
                l += 1
            b2[ord(s2[r]) - ord("a")] += 1
            print(l, r, b2)
            if b1 == b2: return True
            r += 1
                
            
        return False
            
        