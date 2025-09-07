class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write_index = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index
    
# Example usage:
a = Solution()
print(a.removeDuplicates([1,1,1,2,2,3]))  # Output: 5
print(a.removeDuplicates([0,0,1,1,1,1,2,3,3]))  # Output: 7
        