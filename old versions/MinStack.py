class MinStack:
    class StackNode:
        def __init__(self, val, least):
            self.val = val
            self.least = least



    def __init__(self):
        self.lowest = None
        self.stack = []

    def push(self, val: int) -> None:
        n = self.StackNode(val, self.lowest)
        if self.lowest is None:
            self.lowest = val
        if val < self.lowest:
            self.lowest = val
        self.stack.insert(0,n)
        

    def pop(self) -> None:
        n = self.stack[0]
        self.stack.pop(0)
        self.lowest = n.least
        return n.val

    def top(self) -> int:
        return self.stack[0].val
        

    def getMin(self) -> int:
        return self.lowest
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
# print(obj.lowest)
obj.push(0)
# print(obj.lowest)
obj.push(-3)
# print(obj.lowest)
print(obj.getMin())
obj.pop()
print(obj.top())



