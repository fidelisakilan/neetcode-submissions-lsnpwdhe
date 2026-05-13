class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        seq = []

        def dfs(i):
            if i == len(s):
                res.append(seq[::])
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    seq.append(s[i:j+1])
                    dfs(j+1)
                    seq.pop() 
        dfs(0)
        return res