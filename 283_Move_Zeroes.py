class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums[::-1]:
            if i == 0:
                nums.remove(i)
                nums.append(0)

# Example usage:
a = Solution()
print(a.moveZeroes([0,1,0,3,12]))  # Output: [1,3,12,0,0]
print(a.moveZeroes([0]))  # Output: [0]
