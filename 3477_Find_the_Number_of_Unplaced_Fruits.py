class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        unplacedFruits = len(fruits)
        fill_basket = ['empty'] * len(baskets)
        
        for fruit in fruits:
            for index, basket in enumerate(baskets):
                if fruit <= basket and fill_basket[index] == 'empty':
                    unplacedFruits -= 1
                    fill_basket[index] = 'filled'
                    break
        return unplacedFruits

a = Solution()
print(a.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]))
print(a.numOfUnplacedFruits([3,6,1], baskets = [6,4,7]))