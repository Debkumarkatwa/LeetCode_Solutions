class Bank:

    def __init__(self, balance: list[int]):
        self.balance = [0] + balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.balance) - 1 or account2 > len(self.balance) - 1 or self.balance[account1] < money:
            return False
        
        self.balance[account1] -= money
        self.balance[account2] += money
        return True
    
    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance) - 1:
            return False
        
        self.balance[account] += money
        return True
    
    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance) - 1 or self.balance[account] < money:
            return False
        
        self.balance[account] -= money
        return True


bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10))     # True
print(bank.transfer(5, 1, 20))  # True
print(bank.deposit(5, 20))      # True
print(bank.transfer(3, 4, 15))  # False
print(bank.withdraw(10, 50))    # False