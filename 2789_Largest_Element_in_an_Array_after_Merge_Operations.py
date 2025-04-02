class Solution:
    def maxArrayValue(self, nums: list[int]) -> int:
        big = [0, 0]
        a = True
        while a == True:
            for i in range(len(nums) - 1, 0, -1):
                if (nums[i] >= nums[i - 1]):
                    big = [(nums[i] + nums[i - 1]), i-1]
                    
                    nums.pop(big[1])
                    nums[big[1]] = big[0]
                    break
            else:
                a = False
            # print(nums)

        return max(nums)


a = Solution()
print(a.maxArrayValue([2,3,7,9,3])) # 21
print(a.maxArrayValue([5,3,3])) # 11
print(a.maxArrayValue([40,15,35,98,77,79,24,62,53,84,97,16,30,22,49]))
