class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
            elif tok == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif tok == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b/a)
            elif tok == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a*b)
            else:
                stack.append(tok)
        
        return int(stack[0])