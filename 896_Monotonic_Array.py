class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        indicator = None
        for i in range(len(nums) - 1):
            if indicator is None:
                if nums[i] < nums[i + 1]:
                    indicator = 'increasing'
                elif nums[i] > nums[i + 1]:
                    indicator = 'decreasing'
                continue

            if indicator == 'increasing' and nums[i] > nums[i + 1]:
                return False
            if indicator == 'decreasing' and nums[i] < nums[i + 1]:
                return False
            
        return True


a = Solution()
print(a.isMonotonic([1,2,2,3]))     # true
print(a.isMonotonic([6,5,4,4]))     # true
print(a.isMonotonic([1,3,2]))     # false