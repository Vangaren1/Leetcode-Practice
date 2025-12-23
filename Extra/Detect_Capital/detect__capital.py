from typing import Optional, List
import string


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0] in string.ascii_uppercase:
            return all([ch in string.ascii_uppercase for ch in word[1:]]) or all(
                [ch in string.ascii_lowercase for ch in word[1:]]
            )
        return all([ch in string.ascii_lowercase for ch in word[1:]])
        pass


if __name__ == "__main__":
    sol = Solution()

    word = "FlaG"
    print(sol.detectCapitalUse(word))
    word = "USA"
    print(sol.detectCapitalUse(word))
    print("Running Solution...")
