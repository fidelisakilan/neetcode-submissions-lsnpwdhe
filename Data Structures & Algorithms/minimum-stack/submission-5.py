class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currMin = float("infinity")
        

    def push(self, val: int) -> None:
        self.currMin = min(val, self.currMin)
        self.stack.append(val)
        self.minStack.append(self.currMin)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.currMin = self.minStack[-1]
        else:
            self.currMin = float("infinity")
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
