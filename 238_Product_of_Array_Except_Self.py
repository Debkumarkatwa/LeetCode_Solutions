class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        for i in range(1,len(nums)):   # here we calculate the product of the previous elements of selected index (not the behind elements)
            result[i] = result[i-1] * nums[i-1]  # ex :- [1,2,3,4] => [1,1*1,1*2,2*3] => [1,1,2,6]
        
        a = 1
        for j in range(len(nums)-2,-1,-1): # here we calculate the product of the next elements of selected index from last index
            a *= nums[j+1]                 # ex :- [1,2,3,4] => [12*2,4*3,1*4,1] => [24,12,4,1]
            result[j] *= a                 # result = [1,1,2,6] * [24,12,4,1] => [1*24,1*12,2*4,6*1]

        return result


a = Solution()
print(a.ProductExceptSelf(nums=[1,2,3,4]))      # [24,12,8,6]
print(a.ProductExceptSelf(nums=[-1,1,0,-3,3]))  #[0,0,9,0,0]