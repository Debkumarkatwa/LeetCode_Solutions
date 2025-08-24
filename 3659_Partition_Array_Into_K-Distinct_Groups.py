import collections
class Solution:
    def partitionArray(self, nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
                return False

        count = collections.Counter(nums)
            
        if max(count.values()) > len(nums) // k:
            return False

        return True
    
a = Solution()
print(a.partitionArray([3,3,3,3,4,4,4,4], 2))  # Output: True
print(a.partitionArray([1,2,3,4], 3))  # Output: False
print(a.partitionArray([1,2,2,1,3,3], 3))  # Output: True