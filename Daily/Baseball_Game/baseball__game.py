from typing import Optional, List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        curr = []

        for op in ops:
            if op not in ("C", "D", "+"):
                curr.append(int(op))
                continue
            if op == "+":
                curr.append(curr[-1] + curr[-2])
            elif op == "C":
                curr.pop()
            else:
                curr.append(curr[-1] * 2)
        return sum(curr)

        pass


if __name__ == "__main__":
    sol = Solution()
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(sol.calPoints(ops))
    print("Running Solution...")
