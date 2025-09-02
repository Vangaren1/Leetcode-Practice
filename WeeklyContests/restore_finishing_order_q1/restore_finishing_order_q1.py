from typing import Optional, List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []
        for o in order:
            if o in friends:
                result.append(o)
        return result


if __name__ == "__main__":
    sol = Solution()
    order = [3, 1, 2, 5, 4]
    friends = [1, 3, 4]
    print(sol.recoverOrder(order, friends))
    print("Running Solution...")
