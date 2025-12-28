from typing import Optional, List


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        suffix = [0] * (n + 1)
        for index in range(n - 1, -1, -1):
            suffix[index] = suffix[index + 1] + (customers[index] == "Y")

        prefix = 0

        penaltyCount = [0] * (n + 1)
        best = 0
        for index in range(n + 1):
            penaltyCount[index] = prefix + suffix[index]
            if index < n and customers[index] == "N":
                prefix += 1
            if penaltyCount[index] < penaltyCount[best]:
                best = index

        return best


if __name__ == "__main__":
    sol = Solution()

    assert sol.bestClosingTime("YYNY") == 2
    # assert sol.bestClosingTime("NNNNN") == 0
    # assert sol.bestClosingTime("YYYY") == 4
    print("Running Solution...")
