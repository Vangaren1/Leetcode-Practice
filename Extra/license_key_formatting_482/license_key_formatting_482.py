from typing import Optional, List


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        char = "".join(s.split("-"))

        l = len(char)
        offset = l % k

        retStr = ""
        if offset > 0:
            retStr = char[:offset] + "-"

        count = 0
        for index in range(offset, l):
            retStr += char[index].upper()
            count += 1
            if count == k and index != (l - 1):
                retStr += "-"
                count = 0

        if retStr[-1] == "-":
            return retStr[:-1]
        return retStr


if __name__ == "__main__":
    sol = Solution()

    s = "5F3Z-2e-9-w"
    k = 4
    print(sol.licenseKeyFormatting(s, k))

    s = "2"
    k = 2
    print(sol.licenseKeyFormatting(s, k))
    print("Running Solution...")
