class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        all_sum = sum(range(len(nums)+1))
        # all_sum = (len(nums) * (len(nums) + 1)) // 2
        nums_sum = sum(nums)

        return all_sum - nums_sum
    

a = Solution()
print(a.missingNumber([3,0,1])) # 2
print(a.missingNumber([0,1])) # 2
print(a.missingNumber([9,6,4,2,3,5,7,0,1])) # 8