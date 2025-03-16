# ''' 
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    return [i,j]
# ''' 
class Solution:
    def twoSum(self, nums: list, target: int):
        for i in range(len(nums)):
            a = list(map(lambda x: x + nums[i], nums))
            a.pop(i)
            
            if target in a:
                return[i,nums.index(target-nums[i])]
# ''' 

a = Solution()
print(a.twoSum([2,7,11,15],9)) # [0,1]
print(a.twoSum([3,2,4],6)) # [1,2]