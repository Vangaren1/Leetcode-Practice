from typing import Optional, List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [
            0,
        ] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            if len(stack) == 0 or stack[-1][1] > temp:
                stack.append((index, temp))
                continue
            while stack and stack[-1][1] < temp:
                idx, tmp = stack.pop()
                res[idx] = index - idx
            stack.append((index, temp))

        return res


if __name__ == "__main__":
    sol = Solution()
    temperatures = [30, 38, 30, 36, 35, 40, 28]
    print(sol.dailyTemperatures(temperatures))
    print("Running Solution...")
