from typing import Optional, List


class Solution:
    def numDecodings(self, s: str) -> int:
        seen = {"": 1, "0": 0}

        def dfs(substring):

            if substring in seen:
                return seen[substring]
            if substring[0] == "0":
                return 0
            if len(substring) == 1:
                return 1
            secondAlso = substring[:2]
            if int(secondAlso) > 26:
                secondAlso = None
            total = dfs(substring[1:])
            if secondAlso:
                total += dfs(substring[2:])
            seen[substring] = total
            return total

        return dfs(s)


if __name__ == "__main__":
    sol = Solution()
    s = "111111111111111111111111111111111111111111111"
    expected = 2
    print(sol.numDecodings(s))
    s = "01"
    expected = 0
    print(sol.numDecodings(s))
    print("Running Solution...")
