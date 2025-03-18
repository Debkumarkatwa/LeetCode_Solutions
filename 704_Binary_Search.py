# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         return -1

class Solution:
    def search(self, nums: list[int], target: int) -> int:   
        return self.binary_search(nums, 0, len(nums)-1, target)
    
    def binary_search(self, nums: list[int], low: int, high: int, target: int) -> int:
            if low > high:    return -1       
            
            mid = (low + high) // 2       
            if nums[mid] > target:
                return self.binary_search(nums, low, mid-1, target)
            elif nums[mid] < target:
                return self.binary_search(nums, mid+1, high, target)
            else:
                return mid

a = Solution()
print(a.search(nums = [-1,0,3,5,9,12], target = 9)) # 4
print(a.search(nums = [-1,0,3,5,9,12], target = 2)) # -1
print(a.search(nums = [5], target = 5)) # 0
print(a.search(nums = [-1,0,3,5,9,12], target = 2)) # -1