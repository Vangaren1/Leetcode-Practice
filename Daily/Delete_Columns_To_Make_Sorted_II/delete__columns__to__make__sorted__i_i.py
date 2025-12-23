from typing import Optional, List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def check(arr):
            return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

        if check(strs):
            return 0

        if len(strs[0]) < 2:
            return 0

        pass


if __name__ == "__main__":
    sol = Solution()
    strs = [
        "ca",
        "bb",
        "ac",
    ]
    print(sol.minDeletionSize(strs))
    print("Running Solution...")
