from typing import Optional, List


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.isEmpty():
            currMin = self.getMin()
            if val < currMin:
                currMin = val
            self.stack.insert(0,(val, currMin))
        else:
            self.stack.insert(0,(val,val))

    def pop(self) -> None:
         self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0][0]

    def getMin(self) -> int:
        return self.stack[0][1]
        
    def isEmpty(self) -> bool:
        return len(self.stack) == 0
        

if __name__ == "__main__":
    m = MinStack()
    m.push(-2)
    m.push(0)
    m.push(-3)
    print(m.getMin())
    m.pop()
    print(m.top())
    print(m.getMin())
    print("Running Solution...")
