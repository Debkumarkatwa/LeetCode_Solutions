class ATM:
    note =       [20,50,100,200,500]
    note_count = [ 0, 0,  0,  0,  0]

    def deposit(self, banknotesCount: list[int]) -> None:
        self.note_count = list(map(lambda x, y: x + y, self.note_count, banknotesCount))

    def withdraw(self, amount: int) -> list[int]:
        if amount % 10 != 0:    return [-1]

        count = self.note_count.copy()
        result = [0,0,0,0,0]

        for i in range(4,-1,-1):
            result[i] = min(count[i], amount // self.note[i])
            amount -= result[i] * self.note[i]
            count[i] -= result[i]

        if amount == 0:
            self.note_count = count
            return result
        return [-1]


atm = ATM()
print(atm.deposit([0,0,1,2,1])    )# null
print(atm.withdraw(600)           )# [0,0,1,0,1]
print(atm.deposit([0,1,0,2,1])    )# null
print(atm.withdraw(600)           )# [-1]
print(atm.withdraw(550)           )# [0,1,0,0,1)]