from typing import Optional, List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)

        if n in (0, 1):
            return n

        total = 0

        ptr1, ptr2 = 0, 0
        last = prices[0]
        while ptr1 < n and ptr2 < n:

            ptr2 += 1

            # if the next element is a smooth descent, keep checking

            if ptr2 < n and last - prices[ptr2] == 1:
                last = prices[ptr2]
                continue

            # if not, calculate the period of smooth descent from ptr1 and ptr2-1
            # and reset ptr1/ptr2

            if ptr2 < n:
                last = prices[ptr2]
            lengthOfDescent = ptr2 - ptr1
            total += (lengthOfDescent * (lengthOfDescent + 1)) // 2
            ptr1 = ptr2

        return total


if __name__ == "__main__":
    sol = Solution()

    prices = [8, 6, 7, 7]

    print(sol.getDescentPeriods(prices))
    print("Running Solution...")
