class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        a = len(nums[0])
        c = []
        for i in range(len(nums)):
            b = bin(i)[2:].zfill(a)
            if str(b) not in nums:
                return b
            
            c.append(int(nums[i], 2))
        b = max(c)
        return bin(b+1)[2:].zfill(a)
        

a = Solution()
print(a.findDifferentBinaryString(["01","10"])) # "11"
print(a.findDifferentBinaryString(["00","01"])) # "11"
print(a.findDifferentBinaryString(["111","011","001"])) # "101"