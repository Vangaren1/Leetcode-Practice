from typing import Optional, List
import heapq
from collections import defaultdict


class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        span = 1

        while self.stk and self.stk[-1][0] <= price:
            _, previous_span = self.stk.pop()
            span += previous_span

        self.stk.append((price, span))
        return span


if __name__ == "__main__":
    sol = StockSpanner()
    prices = [7, 2, 1, 2, 2]
    for p in prices:
        print(sol.next(p))
    print("Running Solution...")
