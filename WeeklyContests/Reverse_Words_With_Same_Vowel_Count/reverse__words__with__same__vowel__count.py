from typing import Optional, List


class Solution:
    def reverseWords(self, s: str) -> str:

        wordArray = s.split()

        vowels = "aeiou"

        def vCount(w: str):
            return (
                w.count("a") + w.count("e") + w.count("i") + w.count("o") + w.count("u")
            )

        firstCount = vCount(wordArray[0])

        for index in range(1, len(wordArray)):
            if vCount(wordArray[index]) == firstCount:
                wordArray[index] = wordArray[index][::-1]

        return " ".join(wordArray)

        pass


if __name__ == "__main__":
    sol = Solution()
    # s = "cat and mice"
    # print(sol.reverseWords(s))
    s = "book is ecin"
    print(sol.reverseWords(s))
    print("Running Solution...")
