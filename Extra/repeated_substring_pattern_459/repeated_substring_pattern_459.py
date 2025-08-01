from typing import Optional, List
from collections import defaultdict


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        tmp = ""

        for i in range(0, len(s) // 2):
            tmp += s[i]
            if len(s) % len(tmp) == 0:
                repeatSize = len(s) // len(tmp)
                if tmp * repeatSize == s:
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    test = [
        ("babbabbabbabbab", True),
        ("abaa", False),
        ("abab", True),
        ("abcabcabcabc", True),
    ]
    for t in test:
        assert sol.repeatedSubstringPattern(t[0]) == t[1]
    # print(sol.repeatedSubstringPattern(s))
    print("Running Solution...")
