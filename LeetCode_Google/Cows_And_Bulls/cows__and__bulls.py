from typing import Optional, List
import heapq
from collections import defaultdict, Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        sCount = Counter(secret)
        gCount = Counter(guess)
        matching = 0
        for index, val in enumerate(secret):
            if guess[index] == val:
                sCount[val] -= 1
                gCount[val] -= 1
                if sCount[val] == 0:
                    del sCount[val]
                if gCount[val] == 0:
                    del gCount[val]
                matching += 1

        bullCount = 0

        for key, val in gCount.items():
            if key in sCount:
                bullCount += min(sCount[key], gCount[key])

        return f"{matching}A{bullCount}B"

        pass


if __name__ == "__main__":
    sol = Solution()
    secret = "1123"
    guess = "0111"
    print(sol.getHint(secret, guess))
    secret = "1807"
    guess = "7810"
    print(sol.getHint(secret, guess))
    print("Running Solution...")
