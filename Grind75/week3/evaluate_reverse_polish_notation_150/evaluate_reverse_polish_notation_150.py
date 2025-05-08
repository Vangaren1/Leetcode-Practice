from typing import Optional, List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token.isalnum() or (token[0] == '-' and len(token) > 1):
                stack.insert(0, int(token))
            else:
                first = stack.pop(0)
                second = stack.pop(0)
            
                if token == '+':
                    stack.insert(0, second + first )
                elif token == '*':
                    stack.insert(0, second * first )
                elif token == '-':
                    stack.insert(0, second - first)
                elif token == '/':
                    stack.insert(0, int(second / first) )
        
        return stack[0]

if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    s = Solution()
    expected = 22
    
    assert s.evalRPN(tokens) == expected
    
    print("Running Solution...")
