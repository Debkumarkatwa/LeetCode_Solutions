class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        l = len(nums)
        m = 0
        for i in range(l-2):
            for j in range(i+1,l-1):
                for k in range(j+1,l):
                    a = (nums[i] - nums[j]) * nums[k]
                    if a > m:
                        m = (nums[i] - nums[j]) * nums[k]

        return m
    

a = Solution()
print(a.maximumTripletValue([12,6,1,2,7])) # 77
print(a.maximumTripletValue([1,10,3,4,19])) # 133
print(a.maximumTripletValue([1,2,3])) # 0
