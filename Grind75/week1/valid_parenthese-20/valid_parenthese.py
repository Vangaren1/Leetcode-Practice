class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '{':'}',
            '[':']',
            '(':')'
        }
        for item in s:
            if item in pairs:
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop(-1)
                if item != pairs[top]:
                    return False
                
        return len(stack) == 0
    

sol = Solution()


s = "()[]{}"
assert sol.isValid(s) == True

s = "(]"
assert sol.isValid(s) == False