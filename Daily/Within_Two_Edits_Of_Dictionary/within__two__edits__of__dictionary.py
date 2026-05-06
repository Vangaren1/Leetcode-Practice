from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        results = []

        for q in queries:
            for word in dictionary:
                diff = 0
                for index in range(len(word)):
                    if q[index] != word[index]:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    results.append(q)
                    break

        return results


if __name__ == "__main__":
    sol = Solution()
    queries = ["word", "note", "ants", "wood"]
    dictionary = ["wood", "joke", "moat"]
    print(sol.twoEditWords(queries, dictionary))
    print("Running Solution...")


"""
            class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        dset = set(dictionary)

        def check(word, remaining):
            if remaining == 0 or word in dset:
                return word in dset
            n = len(word)
            for i in range(n):
                for dword in dset:
                    tmp = word[:i] + dword[i] + word[i + 1 :]
                    if check(tmp, remaining - 1):
                        return True
            return False

        return [q for q in queries if check(q, 2)]

            """
