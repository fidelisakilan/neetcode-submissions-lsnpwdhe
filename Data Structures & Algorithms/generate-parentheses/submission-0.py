class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if open == close == n, then that is a valid string
        # if open < n then add a parathesis and backtrack
        # if close < open then add closing parantheis and backtrack
        stack = []
        res = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        backtrack(0,0)
        return res

        