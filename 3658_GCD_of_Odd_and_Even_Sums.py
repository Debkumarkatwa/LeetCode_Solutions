import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd, sumEven = 0, 0
        for num in range(1,n*2+1):
            if num % 2 == 0:
                sumEven += num
            else:
                sumOdd += num

        return math.gcd(sumOdd, sumEven)
            
a = Solution()
print(a.gcdOfOddEvenSums(4))  # Output: 4
print(a.gcdOfOddEvenSums(5))  # Output: 5
print(a.gcdOfOddEvenSums(1009))  # Output: 1