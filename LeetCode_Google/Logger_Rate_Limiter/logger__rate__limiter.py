from typing import Optional, List
import heapq
from collections import defaultdict


class Logger:

    def __init__(self):
        self.lastUsed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        lused = self.lastUsed.get(message, -10)

        if timestamp - lused >= 10:
            self.lastUsed[message] = timestamp
            return True
        return False


if __name__ == "__main__":
    sol = Logger()
    cmd = [
        sol.shouldPrintMessage(1, "foo"),
        sol.shouldPrintMessage(2, "bar"),
        sol.shouldPrintMessage(3, "foo"),
        sol.shouldPrintMessage(8, "bar"),
        sol.shouldPrintMessage(10, "foo"),
        sol.shouldPrintMessage(11, "foo"),
    ]
    for c in cmd:
        print(c)
    print("Running Solution...")
