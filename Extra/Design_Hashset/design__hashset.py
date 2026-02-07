from typing import Optional, List
import heapq
from collections import defaultdict


class MyHashSet:

    def __init__(self):
        self.array = [False] * (10**6)

    def add(self, key: int) -> None:
        self.array[key] = True

    def remove(self, key: int) -> None:
        self.array[key] = False

    def contains(self, key: int) -> bool:
        return self.array[key]


if __name__ == "__main__":
    sol = MyHashSet()

    print("Running Solution...")
