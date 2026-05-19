from typing import Optional, List
import heapq
from collections import defaultdict, Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            while count[card] > 0:
                for x in range(card, card + groupSize):
                    if count[x] == 0:
                        return False
                    count[x] -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")


"""_summary_

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        currSize = 1
        last = hand.pop(0)
        ptr = 0

        while hand and ptr < len(hand):
            if currSize == groupSize:
                currSize = 0
                ptr = 0
                last = -1
                continue
            if hand[ptr] == last + 1 or last == -1:
                last = hand.pop(ptr)
                currSize += 1
                continue
            ptr += 1

        return currSize == groupSize and len(hand) == 0

        """
