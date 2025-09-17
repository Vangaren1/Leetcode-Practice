from typing import Optional, List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        t = [i[0] + i[1] for i in tasks]
        return min(t)


if __name__ == "__main__":
    sol = Solution()
    tasks = [[1, 6], [2, 3]]
    print("Running Solution...")
