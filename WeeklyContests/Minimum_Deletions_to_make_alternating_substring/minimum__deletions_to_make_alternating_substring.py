from typing import Optional, List


class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        def minDel(s: str) -> int:
            deletions = 0
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    deletions += 1
            return deletions

        results = []
        s = list(s)
        for q in queries:
            if q[0] == 1:
                idx = q[1]
                if s[idx] == "A":
                    s[idx] = "B"
                else:
                    s[idx] = "A"
            elif q[0] == 2:
                l, r = q[1], q[2]
                results.append(minDel(s[l : r + 1]))

        return results

        pass


if __name__ == "__main__":
    sol = Solution()

    s = "ABA"
    queries = [[2, 1, 2], [1, 1], [2, 0, 2]]

    print(sol.minDeletions(s, queries))

    print("Running Solution...")
