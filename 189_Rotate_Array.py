class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k is greater than n

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
    
        reverse(0, n - 1)   # Step 1: Reverse the entire array  
        reverse(0, k - 1)   # Step 2: Reverse the first k elements
        reverse(k, n - 1)   # Step 3: Reverse the remaining n-k elements

        return nums
    
    
a = Solution()
print(a.rotate([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]
print(a.rotate([-1,-100,3,99], 2)) # [3,99,-1,-100]