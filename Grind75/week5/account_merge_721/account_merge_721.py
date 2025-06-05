from typing import Optional, List
from collections import defaultdict
class QuickUnion:
    
    def __init__(self, size):
        self.id = [ i for i in range(size) ]
        
    def root(self, index):
        while index != self.id[index]:
            self.id[index] = self.id[self.id[index]] 
            index = self.id[index]
        return index

    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        rootP = self.root(p)
        rootQ = self.root(q)
        self.id[rootP] = rootQ


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        qu = QuickUnion(len(accounts))
        
        emailToAccount = {}
        
        for index, acct in enumerate(accounts):
            for email in acct[1:]:
                if email in emailToAccount:
                    qu.union(index, emailToAccount[email])
                else:
                    emailToAccount[email] = index 
        
        newAcct = defaultdict( list )
        
        for email, index in emailToAccount.items():
            leadAcct = qu.root(index)
            newAcct[leadAcct].append(email)
            
        result = []
        
        for index in newAcct.keys():
            name = accounts[index][0]
            e = newAcct.get(index)
            e.sort()
            e.insert(0,name)
            result.append( e )
        
        return result

if __name__ == "__main__":
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    s = Solution()
    
    result = s.accountsMerge( accounts )
    for r in result:
        print(r)
    print("Running Solution...")
