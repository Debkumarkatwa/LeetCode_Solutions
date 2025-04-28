class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = 0
        max_sum = nums[0]

        for index in range(len(nums)):
            current_sum += nums[index]

            if current_sum > max_sum:
                max_sum = current_sum

            if current_sum < 0:
                current_sum = 0

        return max_sum        


a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(a.maxSubArray([1,2,3,4,-1,-1,-1,-1]))  # Output: 10
print(a.maxSubArray([1,2,3,4,-1,-1,-1,-1,10]))  # Output: 16