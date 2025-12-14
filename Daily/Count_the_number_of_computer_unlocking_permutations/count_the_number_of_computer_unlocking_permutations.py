from typing import Optional, List
import math


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        first = complexity[0]
        n = len(complexity)

        if min(complexity) != first or first in complexity[1:]:
            return 0

        return (math.factorial(n - 1)) % (10**9 + 7)

        pass


if __name__ == "__main__":
    sol = Solution()
    complexity = [1, 2, 3]
    print(sol.countPermutations(complexity))

    complexity = [3, 3, 3, 4, 4, 4]
    print(sol.countPermutations(complexity))

    print("Running Solution...")
