class MinStack:

    def __init__(self):
        self.stack = []
        self.minEl = None
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minEl = val
        else:
            if val >= self.minEl:
                self.stack.append(val)
            else:
                flag = 2*val - self.minEl
                self.stack.append(flag)
                self.minEl = val
        return

    def pop(self) -> None:
        if not self.stack:
            return 
        else:
            if self.stack[-1] >= self.minEl:
                self.stack.pop()
            else:
                self.minEl = 2*self.minEl - self.stack[-1]
                self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return 
        else:
            if self.stack[-1] >= self.minEl:
                return self.stack[-1]
            else:
                return self.minEl
        
    def getMin(self) -> int:
        if not self.stack:
            return 
        else:
            return self.minEl
        
