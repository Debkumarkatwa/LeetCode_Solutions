class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            current_area = (right - left) * min(height[left], height[right]) # Calculate the area width * height
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49




