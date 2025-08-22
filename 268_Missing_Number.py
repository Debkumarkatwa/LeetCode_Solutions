class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        mis_num = 0
        limit = len(nums)

        for i in range(limit+1):
            mis_num ^= i

        for i in nums:
            mis_num ^= i

        return mis_num


a = Solution()
print(a.missingNumber([3,0,1])) # 2
print(a.missingNumber([0,1])) # 2
print(a.missingNumber([9,6,4,2,3,5,7,0,1])) # 8
        