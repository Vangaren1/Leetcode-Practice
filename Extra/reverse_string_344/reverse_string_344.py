from typing import Optional, List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first = 0
        last = len(s)-1
        while first < last:
            tmp = s[first]
            s[first] = s[last]
            s[last] = tmp
            first += 1
            last -= 1
            

if __name__ == "__main__":
    print("Running Solution...")
