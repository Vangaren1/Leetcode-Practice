from typing import Optional, List


class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        tmp = Queue()
        while self.queue.empty() == False:
            tmp.push(self.queue.pop())
        self.queue.push(x)
        while tmp.empty() == False:
            self.queue.push( tmp.pop())
       
    def pop(self) -> int:
        return self.queue.pop()
        
    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.empty()


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to the back of the queue."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item from the front of the queue."""
        if self.empty():
            raise IndexError("pop from empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the item at the front without removing it."""
        if self.empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def empty(self):
        """Return True if the queue is empty."""
        return len(self.items) == 0


if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    print(s.top())
    print(s.pop())
    print(s.empty())
    print("Running Solution...")
