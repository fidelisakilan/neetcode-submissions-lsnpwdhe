class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = ""
        for letter in s:
            if letter.isalnum():
                new_str = new_str + letter
        s = new_str

        print(s)
        p1 = 0
        p2 = len(s) - 1
        while p1 <= p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True




        