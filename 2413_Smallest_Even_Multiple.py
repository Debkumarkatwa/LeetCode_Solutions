class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n*2
    

a = Solution()
print(a.smallestEvenMultiple(n = 5)) # 10
print(a.smallestEvenMultiple(n = 6))  # 6