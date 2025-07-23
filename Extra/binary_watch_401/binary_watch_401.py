from typing import Optional, List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def display(n: int):
            hours = 0b1111 & (n >> 6)
            minutes = 0b0000111111 & n
            return (hours, minutes)

        retVal = []

        n = 1
        for n in range(1 << 10):
            if bin(n).count("1") == turnedOn:
                hours, minutes = display(n)
                if hours < 12 and minutes < 60:
                    retVal.append("{0}:{1}".format(hours, format(minutes, "02")))
        return retVal


if __name__ == "__main__":
    turnedOn = 1
    expected = [
        "0:01",
        "0:02",
        "0:04",
        "0:08",
        "0:16",
        "0:32",
        "1:00",
        "2:00",
        "4:00",
        "8:00",
    ]

    s = Solution()
    print(s.readBinaryWatch(2))
    print("Running Solution...")
