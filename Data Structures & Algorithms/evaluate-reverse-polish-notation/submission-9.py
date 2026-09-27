class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["-", "+", "*", "/"]
        stack = deque(tokens)
        while len(stack) != 1:
            # print(stack)
            item = stack.popleft()
            if item in operations:
                s2 = int(stack.pop())
                s1 = int(stack.pop())
                if item == "+":
                    res = s1 + s2
                if item == "-":
                    res = s1 - s2
                if item == "*":
                    res = s1 * s2
                if item == "/":
                    res = int(s1 / s2)
                stack.appendleft(str(res))
            else:
                stack.append(item)
        return int(stack[0])