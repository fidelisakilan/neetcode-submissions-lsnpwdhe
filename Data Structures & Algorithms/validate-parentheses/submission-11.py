class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        for l in s:
            print(l)
            if l in list(mapping.values()):
                stack.append(l)
            elif len(stack) != 0:
                popped = stack.pop(-1)
                if mapping[l] != popped:
                    return False
            else:
                return False
        return len(stack) == 0
            
