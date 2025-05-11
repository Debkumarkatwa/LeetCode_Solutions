class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        nums.sort()
        i, j = 0, len(nums) - 1

        while i < j:
            a = nums.count(nums[i])
            b = nums.count(nums[j])

            if a % 2 == 1 or b % 2 == 1:
                return False
            
            i, j = i + a, j - b

        return True


a = Solution()
print(a.divideArray([1,2,3,4])) # false
print(a.divideArray([3,2,3,2,2,2])) # true