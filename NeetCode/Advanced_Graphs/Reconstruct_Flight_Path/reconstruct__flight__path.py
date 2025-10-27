from typing import Optional, List
from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routes = defaultdict(list)
        tickets.sort(reverse=True)

        for src, dst in tickets:
            routes[src].append(dst)

        path = []

        def dfs(src):
            while routes[src]:
                dst = routes[src].pop()
                dfs(dst)
            path.append(src)

        dfs("JFK")

        return path[::-1]


if __name__ == "__main__":
    sol = Solution()
    # tickets = [["HOU", "JFK"], ["SEA", "JFK"], ["JFK", "SEA"], ["JFK", "HOU"]]
    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    print(sol.findItinerary(tickets))

    tickets = [["BUF", "HOU"], ["HOU", "SEA"], ["JFK", "BUF"]]
    print(sol.findItinerary(tickets))
    print("Running Solution...")
