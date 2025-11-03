from typing import Optional, List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ptr1, ptr2 = 0, 1
        total = 0

        while ptr1 < len(colors) - 1:
            if colors[ptr1] == colors[ptr2]:
                while ptr2 < len(colors) and colors[ptr1] == colors[ptr2]:
                    ptr2 += 1
                mVal = max(neededTime[ptr1:ptr2])
                s = sum(neededTime[ptr1:ptr2])
                total += s
                total -= mVal
                ptr1 = ptr2 - 1
            ptr2 += 1
            ptr1 += 1

        return total


if __name__ == "__main__":
    sol = Solution()
    colors = "bbbaaa"
    neededTime = [4, 9, 3, 8, 8, 9]
    print(sol.minCost(colors, neededTime))
    print("Running Solution...")
