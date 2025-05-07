from typing import Optional, List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        start = 0
        seen = set()
        for index in range(len(s)):
            curr = s[index]
            while curr in seen:
                seen.remove(s[start])
                start += 1
            seen.add(curr)
            maximum = max(maximum, index - start + 1)            
        return maximum
        

if __name__ == "__main__":
    s = "abcdec"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
    print("Running Solution...")
