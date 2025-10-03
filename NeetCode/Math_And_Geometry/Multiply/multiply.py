from typing import Optional, List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(n: str) -> int:
            nList = [int(ch) for ch in n]
            tens = 1
            total = 0
            while nList:
                total += nList.pop() * tens
                tens *= 10
            return total

        total = convert(num1) * convert(num2)

        return str(total)


if __name__ == "__main__":
    sol = Solution()
    # num1 = "3"
    # num2 = "4"

    # print(sol.multiply(num1, num2))

    num1 = "111"
    num2 = "222"
    print(sol.multiply(num1, num2))

    print("Running Solution...")
