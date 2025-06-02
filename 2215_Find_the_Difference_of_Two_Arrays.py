class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        return list( [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))] )
        
# Example usage:
a = Solution()
print(a.findDifference([1, 2, 3], [2, 4, 6]))  # Output: [[1, 3], [4, 6]]
print(a.findDifference([1, 2, 3, 3], [2, 4, 6]))  # Output: [[1, 3], [4, 6]]