class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_length, left, zero_count, temp_left = 0, 0, 0, -1

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

                if zero_count == 2:
                    max_length = max(max_length, right - left - 1)
                    left = temp_left + 1
                    zero_count = 1

                temp_left = right # update the position of the last zero

        max_length = max(max_length, len(nums) - left - 1)  # if there is no zero/ only one 0 in the array

        return max_length
    
# Example usage:
solution = Solution()
print(solution.longestSubarray([1,1,0,1]))  # Output: 3
print(solution.longestSubarray([0,1,1,1,0,1,1,0,1]))  # Output: 5
print(solution.longestSubarray([1,1,1]))  # Output: 5
