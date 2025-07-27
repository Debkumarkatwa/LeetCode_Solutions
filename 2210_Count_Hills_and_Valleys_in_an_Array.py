class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        count = []
        for i in range(len(nums[:-1])):
            if nums[i] != nums[i+1]:
                count.append(nums[i])

        count.append(nums[-1])
        nums.clear()

        for index, value in enumerate(count):
            if index == 0 or index == len(count)-1:
                continue

            if value > count[index-1] and value > count[index+1]:
                nums.append('hill')
            if value < count[index-1] and value < count[index+1]:
                nums.append('valley')

        return len(nums)
        

a = Solution()
print(a.countHillValley([2,4,1,1,6,5]))
print(a.countHillValley([6,6,5,5,4,1]))