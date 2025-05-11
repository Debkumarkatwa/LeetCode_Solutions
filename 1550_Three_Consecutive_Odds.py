class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0

        for num in arr:
            if num % 2 != 0:
                count += 1
            else:
                count = 0

            if count == 3:
                return True

        return False
        

a = Solution()
print(a.threeConsecutiveOdds([2, 6, 4, 1]))  # False
print(a.threeConsecutiveOdds([1, 2, 3, 4]))  # False
print(a.threeConsecutiveOdds([1, 2, 3, 5, 7]))  # True