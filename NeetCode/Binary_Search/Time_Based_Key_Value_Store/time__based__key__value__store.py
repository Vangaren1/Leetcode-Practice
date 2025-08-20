from typing import Optional, List
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        array = self.store.get(key)
        return self.binSearch(array, timestamp)

    def binSearch(self, array: list, timestamp: int):
        if array == None or len(array) == 0:
            return ""

        if timestamp < array[0][1]:
            return ""

        left = 0
        right = len(array) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            curr = array[mid][1]
            if timestamp == curr:
                return array[mid][0]
            if timestamp > curr:
                result = array[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result


if __name__ == "__main__":
    sol = TimeMap()
    sol.set("key1", "val1", 10)
    sol.set("key1", "val2", 20)
    sol.set("key1", "val3", 30)
    print(sol.get("key1", 15))
    print(sol.get("key1", 25))
    print(sol.get("key1", 35))
    # sol.set("alice", "sad", 3)
    # print(sol.get("key1", 11))

    print("Running Solution...")
    # ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
