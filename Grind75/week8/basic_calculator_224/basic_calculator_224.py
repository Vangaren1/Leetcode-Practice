from typing import Optional, List

import re


class Solution:
    def calculate(self, s: str) -> int:
        func = {
            "+": lambda a, b: b + a,
            "-": lambda a, b: b - a,
            "/": lambda a, b: b / a,
            "*": lambda a, b: b * a,
        }
        e = re.findall(r"\d+|[()+\-*/]", s)
        # e = self.preprocess_unary_minus(e)
        num = []
        symbols = []
        ops = ("-", "+", "/", "*", "(")
        prev = None
        for c in e:
            if c in ops:
                if prev in ops:
                    num.append(0)
                symbols.append(c)
            elif c.isdigit():
                num.append(c)
            elif c == ")":

                while len(symbols) > 0 and symbols[-1] != "(":
                    n1 = int(num.pop())
                    n2 = int(num.pop())
                    f = symbols.pop()
                    r = func[f](n1, n2)
                    num.append(r)
                symbols.pop()
            prev = c

        while len(num) > 1:
            n1 = int(num.pop(0))
            n2 = int(num.pop(0))
            r = func[symbols.pop(0)](n2, n1)
            num.append(r)
        return num[0]

    def preprocess_unary_minus(self, tokens):
        result = []
        prev = None
        for token in tokens:
            if token == "-" and (
                prev
                in (
                    None,
                    "(",
                    "+",
                    "-",
                    "*",
                    "/",
                )
            ):
                result.extend(["0", "-"])  # Convert unary to binary
            else:
                result.append(token)
            prev = token
        return result


if __name__ == "__main__":
    sol = Solution()

    s = "1-(     -2)"
    print(sol.calculate(s))
    print("Running Solution...")
