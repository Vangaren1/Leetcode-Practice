from typing import Optional, List
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1:
            return 1
        people = defaultdict(list)
        pSet = set(range(1, n + 1))
        for t1 in trust:
            people[t1[1]].append(t1[0])
            if t1[0] in pSet:
                pSet.remove(t1[0])
        for key, item in people.items():
            if key in pSet and len(item) == n - 1:
                return key
        return -1


if __name__ == "__main__":
    sol = Solution()
    n = 3
    trust = [[1, 3], [2, 3]]
    print(sol.findJudge(n, trust))
    print("Running Solution...")
