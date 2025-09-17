from typing import Optional, List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        seen = {}
        seen[("", "")] = 0

        set1 = set(text1)
        set2 = set(text2)
        check = len(set1.intersection(set2))
        if check in (0, 1):
            return check

        def rec(t1, t2):
            if (t1, t2) in seen:
                return seen[(t1, t2)]
            ptr1, ptr2 = 0, 0
            if ptr1 == len(t1) or ptr2 == len(t2):
                return 0
            if t1[ptr1] == t2[ptr2]:
                tmp = 1 + rec(t1[ptr1 + 1 :], t2[ptr2 + 1 :])
                seen[(t1, t2)] = tmp
                return tmp
            first = rec(t1[ptr1 + 1 :], t2)
            second = rec(t1, t2[ptr2 + 1 :])
            tmp = max(first, second)
            seen[(t1, t2)] = tmp
            return tmp

        return rec(text1, text2)


if __name__ == "__main__":
    sol = Solution()
    text1 = "cat"
    text2 = "dog"
    print(sol.longestCommonSubsequence(text1, text2))
    print("Running Solution...")
