#problem link-->> https://leetcode.com/problems/min-stack/description/

class MinStack:
    
    def __init__(self):
        self.minimum = float('inf')
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if val <= self.minimum:
            self.minstack.append(val)
            self.minimum = val
        self.stack.append(val)
        
    def pop(self) -> None:
        check = self.stack.pop()
        if check == self.minstack[-1]:
            self.minstack.pop()
            if self.minstack:
                self.minimum = self.minstack[-1]
            else:
                self.minimum = float('inf')
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        
