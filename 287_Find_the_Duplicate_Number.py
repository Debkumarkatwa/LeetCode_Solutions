class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            
            seen.add(nums[i])
                      
        return -1   # This line is unreachable given the problem constraints.
    

a = Solution()
print(a.findDuplicate([1,3,4,2,2]))  # Output: 2
print(a.findDuplicate([3,1,3,4,2]))  # Output: 3