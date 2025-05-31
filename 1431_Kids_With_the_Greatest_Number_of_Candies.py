class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]
    
# Example usage:
a = Solution()
print(a.kidsWithCandies([2, 3, 5, 1, 3], 3))  # Output: [True, True, True, False, True]
print(a.kidsWithCandies([4, 2, 1, 1, 2], 1))  # Output: [True, False, False, False, False]
print(a.kidsWithCandies([12, 1, 12], 10))  # Output: [True, False, True]