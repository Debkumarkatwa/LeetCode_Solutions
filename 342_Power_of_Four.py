class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n % 4 == 0:
            n //= 4
        return n == 1
        

a = Solution()
print(a.isPowerOfFour(16))  # True
print(a.isPowerOfFour(5))   # False
print(a.isPowerOfFour(1))   # True