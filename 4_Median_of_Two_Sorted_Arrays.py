class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        '''
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
        The overall run time complexity should be O(log (m+n)).
        '''
        nums1.extend(nums2)
        nums1.sort()

        mid_index = len(nums1) // 2
        if len(nums1) % 2 != 0:
            return nums1[mid_index]
        else:
            return (nums1[mid_index] + nums1[mid_index - 1]) / 2


a = Solution()
print(a.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
print(a.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5