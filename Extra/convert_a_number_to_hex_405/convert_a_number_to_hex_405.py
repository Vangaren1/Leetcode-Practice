from typing import Optional, List


class Solution:
    def toHex(self, num: int) -> str:
        h = ""
        hDict = {
            "0000": "0",
            "0001": "1",
            "0010": "2",
            "0011": "3",
            "0100": "4",
            "0101": "5",
            "0110": "6",
            "0111": "7",
            "1000": "8",
            "1001": "9",
            "1010": "a",
            "1011": "b",
            "1100": "c",
            "1101": "d",
            "1110": "e",
            "1111": "f",
        }
        numStr = ""
        if num >= 0:
            numStr = format(num, "032b")
        else:
            numStr = format(num & 0xFFFFFFFF, "032b")

        while len(numStr) > 0:
            tmp = numStr[-4:]
            numStr = numStr[:-4]
            h = hDict[tmp] + h

        while h[0] == "0" and len(h) > 2:
            h = h[1:]
        return h


if __name__ == "__main__":
    s = Solution()
    print(s.toHex(-1))
    print("Running Solution...")
