class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        types = len( set(candyType) )
        candyType = len(candyType)//2

        return types if types < candyType else candyType

        # 1 line solution
        return (min(len(candyType)//2, len(set(candyType))))



a = Solution()
print(a.distributeCandies([1, 1, 2, 2, 3, 3]))  # Output: 3
print(a.distributeCandies([1, 1, 2, 3]))        # Output: 2
print(a.distributeCandies([6, 6, 6, 6]))  # Output: 1