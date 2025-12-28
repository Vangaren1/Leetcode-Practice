from typing import Optional, List


class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        # (odd, even)
        evenOddCount = {}

        def balance(s: str):
            if s in evenOddCount:
                return evenOddCount[s]

            even = 0
            odd = 0
            for index in range(0, len(s) - 1, 2):
                odd += ord(s[index]) - 48
                even += ord(s[index + 1]) - 48
            if len(s) % 2 != 0:
                odd += ord(s[len(s) - 1]) - 48
            evenOddCount[s] = (odd, even)
            return (odd, even)

        count = 0

        for i in range(max(low, 10), high + 1):
            s = str(i)
            odd, even = balance(s[:-1])
            if len(s) % 2 == 0:
                even += ord(s[-1]) - 48
            else:
                odd += ord(s[-1]) - 48
            evenOddCount[s] = (odd, even)
            if even == odd:
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()

    print(sol.countBalanced(429113, 725528))

    # assert sol.countBalanced(1, 100) == 9
    # assert sol.countBalanced(120, 129) == 1
    # assert sol.countBalanced(1234, 1234) == 0
    print("Running Solution...")


"""

Brute Force solution, fails at test case 400.  

print(sol.countBalanced(429113, 725528))


class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        def bal(n):
            if n < 10:
                return False
            even = 0
            odd = 0
            s = str(n)
            for index in range(0, len(s) - 1, 2):
                odd += ord(s[index]) - 48
                even += ord(s[index + 1]) - 48
            if len(s) % 2 != 0:
                odd += ord(s[len(s) - 1]) - 48
            return even == odd

        count = 0
        for i in range(low, high + 1):
            if bal(i):
                count += 1
        return count            
            
            """
