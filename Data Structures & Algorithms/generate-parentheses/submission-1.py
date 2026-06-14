class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        content = []
        def dfs(s, e):
            if s == n and e == n:
                res.append("".join(content))
                return
            if s < n:
                content.append("(")
                dfs(s+1, e)
                content.pop()
            if e < s:
                content.append(")")
                dfs(s, e+1)
                content.pop()
            return
        dfs(0, 0)
        return res