from typing import Optional, List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if n <= 0:
        #     return []
        # if n == 1:
        #     return ["()"]
        # if n == 2:
        #     return ["()()", "(())"]
        # if n == 3:
        #     return ["()()()", "(())()", "()(())", "((()))", "(()())"]

        opened, closed = 0, 0

        stack = []
        res = []

        def recParen(open, closed):
            if open == closed == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                recParen(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(")")
                recParen(open, closed + 1)
                stack.pop()

        recParen(0, 0)
        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.generateParenthesis(4))

    print("Running Solution...")
