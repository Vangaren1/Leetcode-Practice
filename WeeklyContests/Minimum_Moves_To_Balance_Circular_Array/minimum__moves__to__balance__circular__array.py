from typing import Optional, List


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        bTotal = sum(balance)
        if bTotal < 0:
            return -1

        minIndex = float("inf")

        # find the negative balance
        for index in range(n):
            if balance[index] < 0:
                minIndex = index
                break

        # if there was no negative balance, minIndex == float('inf')
        if minIndex == float("inf"):
            return 0

        total = 0
        left, right = minIndex, minIndex
        goal = balance[minIndex]
        dist = 0
        while goal < 0:
            dist += 1
            left -= 1
            right = (right + 1) % n

            leftNum = balance[left]
            rightNum = balance[right]
            if left == right:
                curr = dist * leftNum
            else:
                curr = dist * (leftNum + rightNum)

            if leftNum + rightNum > abs(goal):
                total += dist * abs(goal)
                break
            total += curr
            goal += leftNum + rightNum

        return total

        pass


if __name__ == "__main__":
    sol = Solution()
    balance = [
        30,
        21,
        263,
        107,
        284,
        275,
        205,
        51,
        7,
        -381,
        274,
        24,
        4,
        308,
        18,
        231,
        111,
        71,
        175,
        206,
    ]

    print(sol.minMoves(balance))
    print("Running Solution...")
