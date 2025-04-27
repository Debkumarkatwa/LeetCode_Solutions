class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        neg_count, pos_count = 0, len(nums)
        for i in nums:
            if i < 0:
                neg_count += 1
            elif i > 0:
                break
            pos_count -= 1

        return max(pos_count, neg_count)
    

a = Solution()
print(a.maximumCount(nums = [-2,-1,-1,1,2,3])) # 3
print(a.maximumCount(nums = [-3,-2,-1,0,0,1,2])) # 3
print(a.maximumCount(nums = [5,20,66,1314])) # 4
print(a.maximumCount(nums = [-1,-2,3])) # 2