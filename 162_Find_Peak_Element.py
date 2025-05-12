class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        return nums.index(max(nums))
    
# Example usage
a = Solution()
print(a.findPeakElement([5,4,8,7,10,2]))  # Output: 6
print(a.findPeakElement([8,6,1,5,3]))  # Output: 9
print(a.findPeakElement([1,2,3,4,5]))  # Output: 4