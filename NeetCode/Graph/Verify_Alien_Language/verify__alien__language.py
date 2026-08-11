from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alien = {ch: index for index, ch in enumerate(order)}

        for index in range(len(words) - 1):
            first = words[index]
            second = words[index + 1]

            match = True
            ptr = 0
            while ptr < len(first) and ptr < len(second) and match:
                if alien[first[ptr]] > alien[second[ptr]]:
                    return False
                if alien[first[ptr]] < alien[second[ptr]]:
                    match = False
                ptr += 1

            if match and len(second) < len(first):
                return False

        return True

        pass


if __name__ == "__main__":
    sol = Solution()
    # words = ["dag", "disk", "dog"]
    # order = "hlabcdefgijkmnopqrstuvwxyz"

    # print(sol.isAlienSorted(words, order))

    words = ["neetcode", "neet"]
    order = "worldabcefghijkmnpqstuvxyz"

    print(sol.isAlienSorted(words, order))
    print("Running Solution...")


""" 
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alien = {ch: index for index, ch in enumerate(order)}

        for index in range(len(words) - 1):
            first = words[index]
            second = words[index + 1]

            ptr = 0
            length = min(len(first), len(second))
            diff = False
            for idx in range(length):

                if alien[first[idx]] > alien[second[idx]] and not diff:
                    return False
                if first[idx] != second[idx]:
                    diff = True
            if not diff and len(second) < len(first):
                return False

        return True
"""
