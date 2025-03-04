#problem link-->> https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [] * k
        self.size = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.q.pop(0)
        return True

    def Front(self) -> int:
        return self.q[0] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.q[-1] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
