from typing import Optional, List
import heapq, string
from collections import defaultdict


class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        lower = string.ascii_lowercase
        mMap = {}
        for index, ch in enumerate(lower):
            mMap[ch] = morse[index]
        mSet = set()
        for word in words:
            m = ""
            for ch in word:
                m += mMap[ch]
            mSet.add(m)
        return len(mSet)


if __name__ == "__main__":
    sol = Solution()
    words = ["gin", "zen", "gig", "msg"]
    print(sol.uniqueMorseRepresentations(words))
    print("Running Solution...")
