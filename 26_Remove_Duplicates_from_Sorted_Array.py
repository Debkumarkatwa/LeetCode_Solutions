class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(list(set(nums)))   # set() removes duplicates and nums[:] is used to update the original list(in-place)
        return len(nums)
    

a = Solution()
print(a.removeDuplicates([1,1,2])) # 2
print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5
