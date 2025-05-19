class Solution:
    def triangleType(self, nums: list[int]) -> str:
        a = max(nums)

        if a >= sum(nums) - a:
            return None
        
        if nums[0] == nums[1] == nums[2] :
            return 'equilateral'
            
        if nums[0] != nums[1] != nums[2] :
            return 'scalene '

        return 'isosceles '


# Example usage
a = Solution()
print(a.triangleType(nums=[3,4,5]))