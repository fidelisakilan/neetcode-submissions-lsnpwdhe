class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].upper() != s[j].upper():
                print(i, j, s[i], s[j])
                return False
            i += 1
            j -= 1
        
        return True
        