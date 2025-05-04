class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique_nums = set(nums)
        return len(unique_nums) != len(nums)

a = Solution()
print(a.containsDuplicate([1, 2, 3, 1]))  # Output: True
print(a.containsDuplicate([1, 2, 3, 4]))  # Output: False        