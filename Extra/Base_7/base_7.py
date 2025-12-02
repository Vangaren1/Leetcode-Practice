from typing import Optional, List


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        isNegative = num < 0
        if isNegative:
            num *= -1

        result = ""
        while num > 0:
            rem = num % 7
            result = str(rem) + result
            num -= rem
            num //= 7

        if isNegative:
            result = "-" + result

        return result
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.convertToBase7(100))
    print(sol.convertToBase7(-7))
    print("Running Solution...")
