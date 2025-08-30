class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()     
        result = set()     
        
        for i in range(len(nums) - 2):  
            left, right = i + 1, len(nums) - 1  

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0: 
                    left += 1

                elif current_sum > 0:
                    right -= 1

                else:
                    result.add((nums[i], nums[left], nums[right]))
                    
                    left += 1
                    right -= 1  
        
        return sorted(list(result)) 

