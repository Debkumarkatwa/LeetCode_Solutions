class Solution:
    def ProductExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        for i in range(1,len(nums)):
            result[i] = result[i-1] * nums[i-1]
        
        a = 1
        for j in range(len(nums)-2,-1,-1):
            a *= nums[j+1]
            result[j] *= a

        return result


a = Solution()
print(a.ProductExceptSelf(nums=[1,2,3,4]))      # [24,12,8,6]
print(a.ProductExceptSelf(nums=[-1,1,0,-3,3]))  #[0,0,9,0,0]