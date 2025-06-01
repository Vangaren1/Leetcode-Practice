from typing import Optional, List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        pass

if __name__ == "__main__":
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    s = Solution()
    
    result = s.accountsMerge( accounts )
    for r in result:
        print(r)
    print("Running Solution...")
