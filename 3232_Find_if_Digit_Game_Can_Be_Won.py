class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        single_sum, double_sum = 0, 0

        for i in nums:
            if i < 10:
                single_sum += i
            elif i > 9 and i < 100:
                double_sum += i

        if single_sum == double_sum:
            return False
        
        return True
    

a = Solution()
print(a.canAliceWin([1,2,3,4,10]))  # Output: False
print(a.canAliceWin([1,2,3,4,5,14]))  # Output: True
print(a.canAliceWin([5,5,5,25]))  # Output: True