class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        # return [nums[i] for i in nums]  # S.C:- O(1)
        result = []
        for i in nums:
            result.append(nums[i])

        return result
    

a = Solution()
print(a.buildArray([0,2,1,5,3,4]))  # Output: [0,1,2,4,5,3]
print(a.buildArray([5,0,1,2,3,4]))  # Output: [4,5,0,1,2,3]