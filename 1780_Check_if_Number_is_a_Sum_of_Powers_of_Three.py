class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = 0
        while n > 0:
            if n % 3 == 2:
                return False
            i += 1
            n //= 3
        
        return True
            

a = Solution()
print(a.checkPowersOfThree(12))
print(a.checkPowersOfThree(91))
print(a.checkPowersOfThree(21))
print(a.checkPowersOfThree(31))