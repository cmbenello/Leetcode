class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val_stack:
            min_val = min(self.min_val_stack[-1], val)
        else:
            min_val = val
        self.min_val_stack.append(min_val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_val_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()