class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0

        for num in nums:
            if num + diff in nums and num + 2 * diff in nums:
                count += 1

        return count
    
a = Solution()
print(a.arithmeticTriplets([0, 1, 2, 3, 4], 1))  # Output: 4
print(a.arithmeticTriplets([4, 5, 6, 7, 8], 2))  # Output: 3
print(a.arithmeticTriplets([0, 2, 3, 4, 6], 2))  # Output: 1