from typing import Optional, List


class Solution:
    def countCollisions(self, directions: str) -> int:
        s = directions.lstrip("L").rstrip("R")
        return len(s) - s.count("S")


if __name__ == "__main__":
    sol = Solution()
    directions = "LLRLRLLSLRLLSLSSSS"
    expected = 5

    print(sol.countCollisions(directions))

    directions = "LLRR"
    expected = 0

    print(sol.countCollisions(directions))

    directions = "RLRSLL"
    expected = 5
    print(sol.countCollisions(directions))
    print("Running Solution...")


"""_summary_
        
"SSLSLSLSLSSSS"
        
"""
