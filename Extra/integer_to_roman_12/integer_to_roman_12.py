from typing import Optional, List


class Solution:
    def intToRoman(self, num: int) -> str:
        iMap = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        retString = ""

        # determine ones position
        t = 1
        while num > 0:
            ones = num % 10
            if ones > 0:
                if ones < 4:
                    retString = iMap[1 * t] * ones + retString
                elif ones == 4:
                    retString = iMap[4 * t] + retString
                elif ones == 9:
                    retString = iMap[9 * t] + retString
                else:
                    retString = iMap[5 * t] + iMap[1 * t] * (ones - 5) + retString
            t *= 10
            num -= ones
            num //= 10

        ones = num % 10
        if ones > 0:
            if ones < 4:
                retString = iMap[1000] * ones + retString

        return retString


if __name__ == "__main__":
    sol = Solution()
    n = 1994

    print(sol.intToRoman(n))
    print("Running Solution...")
