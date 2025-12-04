from typing import Optional, List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        start, ptr = 0, 0

        inStr = set()
        longest = -1
        while start < len(s) and ptr < len(s):
            curr = s[ptr]
            if curr in inStr:
                while curr in inStr:
                    inStr.remove(s[start])
                    start += 1
                inStr.add(curr)
            else:
                inStr.add(curr)
            ptr += 1
            longest = max(longest, ptr - start)
        return longest

        pass


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))

    s = "bbbbb"
    print(sol.lengthOfLongestSubstring(s))
    print("Running Solution...")
