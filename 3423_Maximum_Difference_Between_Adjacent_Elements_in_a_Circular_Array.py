class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        max_diff, n = float('-inf'), len(nums)
        
        for i in range(n-1):
            diff = nums[i] - nums[i + 1]
            if diff > max_diff:    
                max_diff = diff

        return max(max_diff, (nums[-1] - nums[0]))


a = Solution()
print(a.maxAdjacentDistance([1,2,4]))
print(a.maxAdjacentDistance([-5,-10,-5]))