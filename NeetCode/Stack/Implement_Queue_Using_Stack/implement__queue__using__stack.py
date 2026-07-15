from typing import Optional, List
import heapq
from collections import defaultdict


class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        tmp = []
        while self.stack:
            tmp.append(self.stack.pop())
        self.stack.append(x)
        while tmp:
            self.stack.append(tmp.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


if __name__ == "__main__":
    sol = MyQueue()
    print("Running Solution...")
