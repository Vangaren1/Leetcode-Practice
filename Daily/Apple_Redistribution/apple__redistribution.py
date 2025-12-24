from typing import Optional, List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApple = sum(apple)

        capacity.sort(reverse=True)

        ptr = 0
        s = 0
        while ptr < len(capacity) and s <= totalApple:
            s += capacity[ptr]
            if s >= totalApple:
                break
            ptr += 1
        return ptr + 1


if __name__ == "__main__":
    sol = Solution()
    apple = [9, 8, 8, 2, 3, 1, 6]
    capacity = [10, 1, 4, 10, 8, 5]

    print(sol.minimumBoxes(apple, capacity))
    print("Running Solution...")
