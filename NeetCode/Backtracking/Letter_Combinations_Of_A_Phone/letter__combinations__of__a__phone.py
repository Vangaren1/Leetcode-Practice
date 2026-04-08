from typing import Optional, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lDict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        results = []

        def dfs(index, word):
            if len(word) == len(digits):
                results.append(word)
                return

            for ch in lDict.get(digits[index]):
                dfs(index + 1, word + ch)

        dfs(0, "")

        return results


if __name__ == "__main__":
    sol = Solution()
    digits = ["2", "", "34"]
    for d in digits:
        print(sol.letterCombinations(d))
    print("Running Solution...")
