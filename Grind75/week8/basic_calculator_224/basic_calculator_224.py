from typing import Optional, List

import re


class Solution:
    class Stack:
        def __init__(self):
            self.stack = []

        def push(self, n):
            self.stack.insert(0, n)

        def pop(self):
            if not self.isEmpty():
                return self.stack.pop(0)

        def isEmpty(self):
            return len(self.stack) == 0

        def peek(self):
            return self.stack[0]

        def size(self):
            return len(self.stack)

    def calculate(self, s: str) -> int:
        func = {
            "+": lambda a, b: b + a,
            "-": lambda a, b: b - a,
            "/": lambda a, b: b / a,
            "*": lambda a, b: b * a,
        }
        funcp = {
            "+": 1,
            "-": 1,
            "/": 2,
            "*": 2,
        }
        exp = re.findall(r"\d+|[()+\-*/]", s)
        opr = ("+", "-", "/", "*")
        stk = self.Stack()
        queue = []

        prev = None
        for token in exp:
            if token.isdigit():
                queue.append(token)
            elif token in opr:
                while (
                    not stk.isEmpty()
                    and stk.peek() in opr
                    and funcp.get(stk.peek(), 0) >= funcp.get(token, 0)
                ):
                    queue.append(stk.pop())
                if token == "-" and (prev in opr or prev == None or prev in ("(",)):
                    queue.append("0")
                stk.push(token)
            elif token == "(":
                stk.push(token)
            elif token == ")":
                while stk.peek() != "(":
                    queue.append(stk.pop())
                stk.pop()
            prev = token

        while not stk.isEmpty():
            queue.append(stk.pop())

        return self.evalRPN(queue)

        # put the str into postfix notation

    def evalRPN(self, tokens: List[str]) -> int:
        stk = self.Stack()

        for token in tokens:
            if token.isalnum() or (token[0] == "-" and len(token) > 1):
                stk.push(int(token))
            else:
                first = stk.pop()
                second = stk.pop()

                if token == "+":
                    stk.push(second + first)
                elif token == "*":
                    stk.push(second * first)
                elif token == "-":
                    stk.push(second - first)
                elif token == "/":
                    stk.push(int(second / first))

        return stk.peek()


if __name__ == "__main__":
    sol = Solution()

    testCases = [
        ("1+5-4", 2),
        ("1 + 1", 2),
        (" 2-1 + 2 ", 3),
        ("(1+(4+5+2)-3)+(6+8)", 23),
        ("0", 0),
        ("-2+ 1", -1),
    ]
    for test in testCases:
        print("results: {}, expected: {}".format(sol.calculate(test[0]), test[1]))
    print("Running Solution...")
