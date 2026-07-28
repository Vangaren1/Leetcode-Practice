from typing import Optional, List
import heapq
from collections import defaultdict
from common.listnode import ListNode, build_list, print_list


class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.maxSize = k
        self.arr = [None for _ in range(k)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.maxSize:
            return False
        self.arr[self.rear] = value
        self.rear += 1
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.rear == 0:
            return False
        self.arr[self.rear - 1] = None
        self.rear -= 1
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.rear == 0:
            return -1
        return self.arr[self.rear - 1]

    def Rear(self) -> int:
        if self.rear == 0:
            return -1
        return self.arr[0]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxSize


if __name__ == "__main__":
    sol = MyCircularQueue()
    print("Running Solution...")
