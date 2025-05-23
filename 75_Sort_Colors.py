class Solution:
    def sortColors(self, nums: list[int]) -> None:
        '''        This is the Dutch National Flag algorithm.        
        low = mid = 0
        high = len(nums) - 1
        
        while(mid <= high):
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        '''
        d = {}
        for i in nums:    
            d[i] = d.get(i,0) + 1

        nums.clear()
        for i in range(3):
            if i in d:
                nums.extend([i] * d[i])



a = Solution()
x = [2,0,2,1,1,0]
a.sortColors(x)
print(x)