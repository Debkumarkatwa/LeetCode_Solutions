class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n % 3 == 0:
            n //= 3
        return n == 1
    

a = Solution()
print(a.isPowerOfThree(27))  # Output: True
print(a.isPowerOfThree(0))   # Output: False
print(a.isPowerOfThree(9))   # Output: True