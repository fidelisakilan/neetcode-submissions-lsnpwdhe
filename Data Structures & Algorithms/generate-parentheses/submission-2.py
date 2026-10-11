class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # have a count open, count close
        sub = []
        res = []
        def dfs(oc, ec):
            if oc == n and ec == n:
                res.append("".join(sub))
                return
            
            if oc < n:
                sub.append("(")
                dfs(oc+1, ec)
                sub.pop()
            
            if ec < n and ec < oc:
                sub.append(")")
                dfs(oc, ec+1)
                sub.pop()
        dfs(0, 0)
        return res

