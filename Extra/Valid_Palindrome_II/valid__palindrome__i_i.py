from typing import Optional, List


class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        def check(word, skipped=False):
            if len(word) in (0, 1) and skipped:
                return True

            if skipped and word[0] != word[-1]:
                return False

            if word[0] == word[-1] and len(word) > 2:
                return check(word[1:-1], skipped)

            return check(word[1:], True) or check(word[:-1], True)

        return check(s)


if __name__ == "__main__":
    sol = Solution()
    s = "zryxeededexyz"
    print(sol.validPalindrome(s))
    print("Running Solution...")
