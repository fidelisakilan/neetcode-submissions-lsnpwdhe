class MinStack:

    def __init__(self):
        self.currMin = None
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if self.currMin is None:
            self.currMin = val
        else:
            self.currMin = min(self.currMin, val)
        self.stack.append(val)
        self.minStack.append(self.currMin)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.currMin = self.minStack[-1]
        else:
            self.currMin = None

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
