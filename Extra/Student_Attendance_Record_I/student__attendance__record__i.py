from typing import Optional, List


class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") > 1:
            return False

        c = 0
        for ch in s:
            if ch == "L":
                c += 1
                if c == 3:
                    return False
            else:
                c = 0
        return True


if __name__ == "__main__":
    sol = Solution()
    s = "PPALLP"
    print(sol.checkRecord(s))
    print("Running Solution...")
