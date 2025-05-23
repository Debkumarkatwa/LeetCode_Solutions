class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        a, b = [], []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] :
                a.append(nums[i]*2)
                nums[i+1] = 0

            else:
                a.append(nums[i])
        a.append(nums[-1])
        
        for i in a:
            if i != 0:
                b.append(i)
        b.extend(0 for i in range(len(a)-len(b)))
        
        return b
        

a = Solution()
print(a.applyOperations([1,0])) 
print(a.applyOperations([1,2,2,1,1,0])) 
