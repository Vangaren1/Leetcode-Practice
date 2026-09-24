from typing import Optional, List
import heapq, random
from collections import defaultdict


class RandomizedSet:

    def __init__(self):
        self.container = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.container:
            return False
        self.arr.append(val)
        self.container[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.container:
            return False
        index = self.container[val]
        lastItem = self.arr[-1]
        self.arr[-1], self.arr[index] = self.arr[index], self.arr[-1]
        self.container[lastItem] = index
        self.arr.pop()
        del self.container[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


if __name__ == "__main__":
    sol = RandomizedSet()
    print("Running Solution...")
