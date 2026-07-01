from typing import Optional, List
import heapq
from collections import defaultdict


class MyHashMap:

    def __init__(self):
        self.capacity = 128
        self.myMap = [[] for _ in range(self.capacity)]
        self.count = 0
        self.minCapacity = 128

    def _rehash(self, newCap):
        if newCap < self.minCapacity:
            return
        newCap = int(newCap)
        newMap = [[] for _ in range(newCap)]

        for bucket in self.myMap:
            for key, val in bucket:
                newMap[key % newCap].append((key, val))
        self.myMap = newMap
        self.capacity = newCap

    def put(self, key: int, value: int) -> None:
        h = key % self.capacity
        if self.get(key) == -1:
            self.myMap[h].append((key, value))
            self.count += 1

            if self.count / self.capacity > 0.7:
                self._rehash(self.capacity * 1.5)
            return

        for index, (k, val) in enumerate(self.myMap[h]):
            if k == key:
                self.myMap[h][index] = (key, value)

    def get(self, key: int) -> int:
        h = key % self.capacity
        for k, val in self.myMap[h]:
            if k == key:
                return val
        return -1

    def remove(self, key: int) -> None:
        h = key % self.capacity

        for index, (k, val) in enumerate(self.myMap[h]):
            if k == key:
                self.myMap[h].pop(index)
                self.count -= 1

                if self.count / self.capacity < 0.3:
                    self._rehash(self.capacity * 0.75)

                return


if __name__ == "__main__":
    sol = MyHashMap()
    print("Running Solution...")


""" 
class MyHashMap:

    def __init__(self):
        self.myMap = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.myMap[key] = value

    def get(self, key: int) -> int:
        return self.myMap[key]

    def remove(self, key: int) -> None:
        self.myMap[key] = -1
"""
