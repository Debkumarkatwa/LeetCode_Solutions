class Cashier:

    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.count = 0

    def getBill(self, product: list[int], amount: list[int]) -> float:
        bill, self.count = 0, self.count + 1
        for j,i in enumerate(product):
            bill += self.prices[self.products.index(i)] * amount[j]
            
        if self.n == self.count:
            bill = bill * ((100 - self.discount) / 100)
            self.count = 0

        return float(bill)



a = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])
print(a.getBill([1, 2], [1, 2])) # 500.0
print(a.getBill([3, 7], [10, 10])) # 4000.0
print(a.getBill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1])) # 800.0
print(a.getBill([4], [10])) # 4000.0
print(a.getBill([7, 3], [10, 10])) # 4000.0
print(a.getBill([7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7])) # 7350.0
print(a.getBill([2, 3, 5], [5, 3, 2])) # 2500.0
