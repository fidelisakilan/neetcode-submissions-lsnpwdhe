class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False
        # First iterated through the letters
        # if open braces, add them to stack
        # if close braces, check if last element in stack matches
        # otherwise return false
        stack = []
        for letter in s:
            if letter in ['(', '[', '{']:
                stack.append(letter)
            elif stack and letter in [')', ']', '}']:
                top = stack.pop()
                if top == "{" and letter == "}":
                    continue
                if top == "[" and letter == "]":
                    continue
                if top == "(" and letter == ")":
                    continue
                return False
            else: 
                return False
        return not len(stack)
                
        