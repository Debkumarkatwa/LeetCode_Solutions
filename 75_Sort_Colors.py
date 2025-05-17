class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
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
