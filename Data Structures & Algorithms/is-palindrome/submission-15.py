class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l <= r:
            print(s[l], s[r])
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].upper() == s[r].upper():
                l += 1
                r -= 1
            else:
                print(s[l], s[r], "0")
                return False
        
        return True
        