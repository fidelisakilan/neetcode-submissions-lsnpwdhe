class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        store1 = [0]*26
        store2 = [0]*26
        
        l = 0
        r = len(s1) - 1

        for i in range(len(s1)):
            store1[ord(s1[i]) - ord('a')] += 1
            store2[ord(s2[i]) - ord('a')] += 1
        

        while r < len(s2):
            print(s2[l:r+1])
            print(1, store1)
            print(2, store2)
            
            if tuple(store1) != tuple(store2):
                store2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            else:
                return True
            
            r += 1
            if r < len(s2):
                store2[ord(s2[r]) - ord('a')] += 1
        return False

