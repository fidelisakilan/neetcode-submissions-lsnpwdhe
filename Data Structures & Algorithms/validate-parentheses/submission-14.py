class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for l in s:
            if l in set(mapping.values()):
                stack.append(l)
            else:
                if stack and mapping[l] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
