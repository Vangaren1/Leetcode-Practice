class myStack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.insert(0, val)

    def pop(self):
        return self.stack.pop(0)

    def top(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0



class MyQueue:

    def __init__(self):
        self.stackA = myStack()
        self.stackB = myStack()

    def push(self, x: int) -> None:
        if self.stackA.empty():
            self.stackA.push(x)
        else:
            while not self.stackA.empty():
                self.stackB.push(self.stackA.pop())
            self.stackA.push(x)
            while not self.stackB.empty():
                self.stackA.push(self.stackB.pop())

    def pop(self) -> int:
        return self.stackA.pop()

    def peek(self) -> int:
        print(self.stackA.stack)
        return self.stackA.top()

    def empty(self) -> bool:
        return self.stackA.empty()


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(5)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()