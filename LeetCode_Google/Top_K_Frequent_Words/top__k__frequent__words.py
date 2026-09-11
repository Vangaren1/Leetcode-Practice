from typing import Optional, List
import heapq
from collections import defaultdict, Counter


class Word:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = Counter(words)

        hq = []

        for word, count in wordCount.items():
            heapq.heappush(hq, (count, Word(word)))

            if len(hq) > k:
                heapq.heappop(hq)

        results = []
        for _ in range(k):
            if hq:
                _, word = heapq.heappop(hq)
                results.append(word.word)
        return results[::-1]


if __name__ == "__main__":
    sol = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(sol.topKFrequent(words, k))
    print("Running Solution...")
