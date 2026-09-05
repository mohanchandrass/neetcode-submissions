class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minstack.append(val)
        else:
            if val<=self.minstack[-1]:
                self.minstack.append(val)
            self.stack.append(val)
        
    def pop(self) -> None:
        if self.stack: 
            if self.top() == self.minstack[-1]:
                self.minstack.pop()
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]   