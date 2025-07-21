from typing import Optional, List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        array = []

        for i in range(1, n + 1):
            tmp = ""
            if i % 3 == 0:
                tmp += "Fizz"
            if i % 5 == 0:
                tmp += "Buzz"
            if len(tmp) > 0:
                array.append(tmp)
            else:
                array.append(str(i))
        return array


if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(10))
    print("Running Solution...")
