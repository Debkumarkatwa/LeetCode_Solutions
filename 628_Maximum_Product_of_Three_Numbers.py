class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        if len(nums) < 3:    # To handle edge case
            return None

        nums.sort()
        # Two possibilities:
        # 1. Product of three largest numbers
        prod1 = nums[-1] * nums[-2] * nums[-3]
        # 2. Product of two smallest (possibly negative) and the largest
        prod2 = nums[0] * nums[1] * nums[-1]

        return prod1 if prod1 > prod2 else prod2
    

a = Solution()
print(a.maximumProduct([-4, 1, -8, 9, 6]))
print(a.maximumProduct([1, 7, 2, -2, 5]))
print(a.maximumProduct([1,2,3]))
        