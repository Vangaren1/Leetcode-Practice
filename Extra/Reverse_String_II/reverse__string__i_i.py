from typing import Optional, List


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if s == "":
            return ""
        return s[:k][::-1] + s[k : 2 * k] + self.reverseStr(s[2 * k :], k)


if __name__ == "__main__":
    sol = Solution()
    s = "abcdefg"
    k = 2
    print(sol.reverseStr(s, k))

    print("Running Solution...")
