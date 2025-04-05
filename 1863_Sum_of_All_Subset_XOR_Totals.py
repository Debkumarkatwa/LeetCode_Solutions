class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        total, n = 0, len(nums)
        # Iterate over all possible subsets using bit manipulation
        for i in range(1 << n):
            xor_sum = 0
            # Calculate the XOR for the current subset
            for j in range(n):
                if i & (1 << j):
                    xor_sum ^= nums[j]
            total += xor_sum
        return total

a = Solution()
print(a.subsetXORSum([1, 3]))  # Output: 6
print(a.subsetXORSum([5, 1, 6]))  # Output: 28
print(a.subsetXORSum([3, 4, 5, 6, 7, 8]))  # Output: 480
        