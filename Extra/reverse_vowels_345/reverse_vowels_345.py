from typing import Optional, List


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','u','o', 'A', 'E', 'I', 'O', "U"]
        s = [ c for c in s ]
        left = 0
        right = len(s)-1

        shifted = False
        while left < right:
            while left < len(s) and s[left] not in vowels:
                shifted = True                
                left += 1
            while right >= 0 and s[right] not in vowels:
                shifted = True
                right -= 1
            if not shifted:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            else:
                shifted = False

        return ''.join(s)

if __name__ == "__main__":
    s = "IceCreAm"
    sol = Solution()
    print(sol.reverseVowels(s))
    print("Running Solution...")
