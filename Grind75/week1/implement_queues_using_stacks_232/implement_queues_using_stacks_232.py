from typing import Optional
from collections import deque

class MyQueue:

    def __init__(self):
        self.mainStack = deque()
        self.tempStack = deque()
        
    def push(self, x: int) -> None:
        while self.mainStack:
            self.tempStack.append(self.mainStack.pop())
        self.mainStack.append(x)
        while self.tempStack:
            self.mainStack.append(self.tempStack.pop())
            
    def pop(self) -> int:
        return self.mainStack.pop()
        
    def peek(self) -> int:
        return self.mainStack[-1]

    def empty(self) -> bool:
        return not self.mainStack
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == "__main__":
    print("Running Solution...")
