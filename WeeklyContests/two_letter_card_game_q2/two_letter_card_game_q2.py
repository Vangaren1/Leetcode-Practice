from typing import Optional, List


class Solution:
    def score(self, cards: List[str], x: str) -> int:
        def diff(a, b, x):
            count = 0
            inA, inB = False, False

            for c1, c2 in zip(a, b):
                if c1 != c2:
                    count += 1
                if c1 == x:
                    inA = True
                if c2 == x:
                    inB = True

            if not inA or not inB:
                return -1
            return count

        def rec(index, hand):
            if len(hand) == 0:
                return 0

            maxCount, count = 0, 0

            if index >= len(hand):
                return count

            # take one card at index
            first = hand.pop(index)
            for idx in range(index, len(hand)):
                count = 0
                # check against each of the remaining cards
                second = hand[idx]
                # check if it's compatible
                check = diff(first, second, x)
                if check != 1:
                    continue

                tmp = hand.pop(idx)
                count = 1 + rec(index, hand.copy())
                hand.insert(idx, tmp)
                maxCount = max(maxCount, count)
            hand.insert(index, first)
            return maxCount

        m = 0
        for index in range(len(cards)):
            m = max(m, rec(index, cards))
        return m


if __name__ == "__main__":
    sol = Solution()
    cards = ["aa", "cb", "ba", "ca", "ac"]
    x = "a"

    print(sol.score(cards, x))
    print("Running Solution...")
