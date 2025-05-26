class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result = []
        if target in nums:   
            nums.sort()
            i = nums.index(target) 

            for index, num in enumerate(nums[i: ]):
                if num != target:
                    break
                result.append(index+i)

        return result
    

a = Solution()
print(a.targetIndices(nums = [1,2,5,2,3], target = 2))  # Output: [1,2]
print(a.targetIndices(nums = [1,2,5,2,3], target = 3))  # Output: [3]
print(a.targetIndices(nums = [1,2,5,2,3], target = 5))  # Output: [4]