class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0

        for i in nums:
            a = len(str(i))

            if a % 2 == 0:
                count += 1

        return count 


a = Solution()
print(a.findNumbers([12,345,2,6,7896]))  # 2
print(a.findNumbers([555,901,482,1771]))  # 1
print(a.findNumbers([1,2,3,4,5,6,7,8,9,100]))  # 0