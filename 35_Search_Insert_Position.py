class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        '''
        using binary search to find the index of the target in a sorted array
        if the target is not found, return the index where it would be inserted in order
        if target < mid it surely placed in that position
        if target > mid it surely placed in the next position
        '''
        start, end, index = 0, len(nums) - 1, 0
        while start <= end:
            mid = (start + end) // 2
            if target > nums[mid] == target:
                end = mid - 1
                index = mid
            elif target < nums[mid]:
                start = index = mid + 1
            else:
                return mid
            
        return index

# Example usage
a = Solution()
print(a.searchInsert(nums = [1,3,5,6], target = 5))  # Output: 2
print(a.searchInsert(nums = [1,3,5,6], target = 2))  # Output: 1
print(a.searchInsert(nums = [1,3,5,6], target = 7))  # Output: 4