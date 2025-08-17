from typing import Optional, List

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        if self.cap == len(self.cache) and key not in self.cache:
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)


if __name__ == "__main__":
    # ["LRUCache", [2], "get", [2], "put", [2, 6], "get", [1], "put", [1, 5], "put", [1, 2], "get", [1], "get", [2]]
    sol = LRUCache(2)
    print(sol.get(2))
    print(sol.put(2, 6))
    print(sol.get(1))
    print(sol.put(1, 5))
    print(sol.put(1, 2))
    print(sol.get(1))
    print(sol.get(2))
    # [null,-1,null,-1,null,null,2,6]
    print("Running Solution...")
