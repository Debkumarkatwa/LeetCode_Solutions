class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        a = []
        for i in nums:
            if i != val:
                a.append(i)
        nums[:] = a
        return len(nums)



a = Solution()
a.removeElement([3,2,2,3], 3) # 2
a.removeElement([0,1,2,2,3,0,4,2], 2) # 5