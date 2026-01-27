from typing import Optional, List


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = [0]

        countZero = s[0] == "0"

        for ch in s:
            if ch == "0" and countZero:
                count[-1] += 1
            elif ch == "1" and countZero:
                count.append(1)
                countZero = False
            elif ch == "0" and not countZero:
                count.append(1)
                countZero = True
            else:
                count[-1] += 1

        ptr = 0
        total = 0
        while ptr < len(count) - 1:
            total += min(count[ptr], count[ptr + 1])
            ptr += 1
        return total


if __name__ == "__main__":
    sol = Solution()
    s = "00100"
    expected = 6

    print(sol.countBinarySubstrings(s))
    print("Running Solution...")
