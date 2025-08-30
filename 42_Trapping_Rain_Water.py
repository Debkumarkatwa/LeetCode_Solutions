class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left ,right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1
                
        return total_water
    

a = Solution()
print(a.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Expected output: 6
print(a.trap([3,0,2,0,4]))  # Expected output: 7
print(a.trap([0,2,0,2]))  # Expected output: 2