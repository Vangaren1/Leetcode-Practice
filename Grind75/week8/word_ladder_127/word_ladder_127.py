from typing import Optional, List

import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        queue = [(beginWord, 1)]

        if endWord not in wordSet:
            return 0

        if len(endWord) != len(beginWord):
            return 0

        if beginWord == endWord:
            return 0

        letters = string.ascii_lowercase

        while queue:

            curr, step = queue.pop(0)

            for index in range(len(curr)):
                for l in letters:
                    tmp = curr[:index] + l + curr[index + 1 :]
                    if tmp in wordSet:
                        if tmp == endWord:
                            return step + 1
                        queue.append((tmp, step + 1))
                        wordSet.remove(tmp)

        return 0


if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(sol.ladderLength(beginWord, endWord, wordList))
    print("Running Solution...")
