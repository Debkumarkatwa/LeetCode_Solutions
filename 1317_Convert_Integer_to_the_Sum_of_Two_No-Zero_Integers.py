class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for A in range(1, n):
            B = n - A
            
            if (A % 10 != 0) and (B % 10 != 0):
                return [A, B]
            
        return []
    

a = Solution()
print(a.getNoZeroIntegers(2))   # [1,1]
print(a.getNoZeroIntegers(11))  # [2,9]
print(a.getNoZeroIntegers(100)) # [1,99]