class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        countT = {}
        window = {}
        for l in t:
            countT[l] = countT.get(l, 0) + 1
        
        l = 0
        have, need = 0, len(countT)
        res = [0,0]
        resLen = float("infinity")
        for r in range(n):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                print(r, l)
                if (r - l + 1) < resLen:
                    resLen = r-l+1
                    res = [l,r]
                window[s[l]] = window.get(s[l], 0) - 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        if resLen == float("infinity"):
            return ""
        return s[res[0]:res[1]+1]

        