from typing import Optional, List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def lex(s):
            last = -1
            for ch in s:
                if ord(ch) < last:
                    return False
                last = ord(ch)
            return True

        total = 0

        for col in range(len(strs[0])):
            s = "".join([c[col] for c in strs])
            if not lex(s):
                total += 1

        return total


if __name__ == "__main__":
    sol = Solution()
    strs = [
        "cba",
        "daf",
        "ghi",
    ]

    print(sol.minDeletionSize(strs))
    print("Running Solution...")
