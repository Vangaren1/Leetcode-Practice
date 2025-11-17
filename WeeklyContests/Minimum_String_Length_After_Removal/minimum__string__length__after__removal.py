from typing import Optional, List


class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        bCount = s.count("b")
        aCount = s.count("a")
        n = len(s)
        total = 0
        while bCount != aCount and len(s) > 0:

            if s[0] == s[-1]:
                if s[-1] == "a":
                    aCount -= 1
                else:
                    bCount -= 1
                s = s[:-1]
            elif aCount > bCount:
                if s[0] == "a":
                    s = s[1:]
                elif s[-1] == "a":
                    s = s[:-1]
                aCount -= 1
            else:
                if s[0] == "b":
                    s = s[1:]
                elif s[-1] == "b":
                    s = s[:-1]
                bCount -= 1
            total += 1

        return total
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "aabbab"
    print(sol.minLengthAfterRemovals(s))
    print("Running Solution...")
