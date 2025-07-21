from typing import Optional, List


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        n1 = [c for c in num1[::-1]]
        n2 = [c for c in num2[::-1]]

        carry = False

        result = ""
        while n1 and n2:
            c1 = n1.pop(0)
            c2 = n2.pop(0)
            car = 1 if carry else 0
            tmp = int(c1) + int(c2) + car
            carry = tmp > 9
            result = result + str(tmp % 10)

        while n1:
            c1 = n1.pop(0)
            car = 1 if carry else 0
            tmp = int(c1) + car
            carry = tmp > 9
            result = result + str(tmp % 10)

        while n2:
            c2 = n2.pop(0)
            car = 1 if carry else 0
            tmp = int(c2) + car
            carry = tmp > 9
            result = result + str(tmp % 10)

        if carry:
            result = result + "1"

        return result[::-1]

        pass


if __name__ == "__main__":
    num1 = "999"
    num2 = "999"

    s = Solution()

    print(s.addStrings(num1, num2))
    print("Running Solution...")
