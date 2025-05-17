class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n] # This copies the elements of nums2 into nums1 starting from index m

        nums1[:] = sorted(nums1)
        # This sorts nums1 in-place


# Example usage
a = Solution()
nums1 = [1,2,4,0,0,0] 
a.merge(nums1 = nums1, m = 3, nums2 = [2,5,6], n = 3)
print(nums1)  