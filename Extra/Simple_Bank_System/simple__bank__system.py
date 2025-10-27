from typing import Optional, List


class Bank:

    def __init__(self, balance: List[int]):
        self.accts = balance
        self.accts.insert(0, 0)
        self.count = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            self.count >= account1
            and self.count >= account2
            and self.accts[account1] >= money
        ):
            self.accts[account1] -= money
            self.accts[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.count >= account:
            self.accts[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.count >= account and self.accts[account] >= money:
            self.accts[account] -= money
            return True
        return False


if __name__ == "__main__":
    accts = [10, 100, 20, 50, 30]
    sol = Bank(accts)

    print(sol.withdraw(3, 10))
    print(sol.transfer(5, 1, 20))
    print(sol.deposit(5, 20))
    print(sol.transfer(3, 4, 15))
    print(sol.withdraw(10, 50))
    print("Running Solution...")
