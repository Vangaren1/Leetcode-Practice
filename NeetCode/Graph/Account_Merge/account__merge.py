from typing import Optional, List
import heapq
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        n = len(accounts)

        qu = QuickUnion(n)

        emailMap = {}
        username = []
        for index, acct in enumerate(accounts):
            username.append(acct[0])
            for email in acct[1:]:
                if email in emailMap:
                    qu.union(index, emailMap[email])
                else:
                    emailMap[email] = index

        newAcct = defaultdict(list)

        for email, index in emailMap.items():
            acct = qu.root(index)
            newAcct[acct].append(email)

        results = []

        for key, arr in newAcct.items():
            arr.sort()
            results.append([username[key]] + arr)
        return results
        pass


class QuickUnion:

    def __init__(self, n: int):
        self.array = [i for i in range(n)]

    def root(self, index):
        while index != self.array[index]:
            self.array[index] = self.array[self.array[index]]
            index = self.array[index]
        return index

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        rootP = self.root(p)
        rootQ = self.root(q)
        self.array[rootP] = rootQ


if __name__ == "__main__":
    sol = Solution()
    accounts = [
        ["neet", "neet@gmail.com", "neet_dsa@gmail.com"],
        ["alice", "alice@gmail.com"],
        ["neet", "bob@gmail.com", "neet@gmail.com"],
        ["neet", "neetcode@gmail.com"],
    ]

    print(sol.accountsMerge(accounts))
    print("Running Solution...")
