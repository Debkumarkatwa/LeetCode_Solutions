from math import factorial
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = str(factorial(n))[::-1]
        count = 0

        while True:
            if ans[count] == '0':
                count += 1
            else:
                return count

# Example usage
a = Solution()
print(a.trailingZeroes(7))  # Output: 701