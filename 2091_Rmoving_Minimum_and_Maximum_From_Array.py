class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        min_i, max_i = nums.index(min(nums)), nums.index(max(nums))
        if min_i > max_i:
            return min(min_i+1, max_i+1+(len(nums)-min_i), len(nums)-max_i)
        else:
            return min(max_i+1, min_i+1+(len(nums)-max_i), len(nums)-min_i)
      



a = Solution()
print(a.minimumDeletions(nums = [2,10,7,5,4,1,8,6]))  # 5 
print(a.minimumDeletions(nums = [0,-4,19,1,8,-2,-3,5]))  # 3
print(a.minimumDeletions(nums = [101]))  # 1