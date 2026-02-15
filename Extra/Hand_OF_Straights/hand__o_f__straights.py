from typing import Optional, List


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

        pass


if __name__ == "__main__":
    sol = Solution()
    hand = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    groupSize = 4
    print(sol.isNStraightHand(hand, groupSize))
    print("Running Solution...")
