#problem link-->> https://leetcode.com/problems/maximum-frequency-stack/description/


class FreqStack:

    def __init__(self):
        self.stack = []
        self.swap = []
        self.counter = defaultdict(int)

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.stack.append(val)
        
    def pop(self) -> int:
        temp1 = max(self.counter.values())
        while self.stack:
            temp2 = self.stack.pop()
            if self.counter[temp2] == temp1:
                ans = temp2
                if self.swap:
                    while self.swap:
                        self.stack.append(self.swap.pop())
                self.counter[ans] -= 1
                return ans
            else:
                self.swap.append(temp2)

        
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
