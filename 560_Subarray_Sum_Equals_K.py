class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_of_sums = 0
        feq = {0:1}
        tempsum = 0

        for i in nums:
            tempsum += i
            
            num_of_sums += feq.get(tempsum - k, 0)
            feq[tempsum] = feq.get(tempsum, 0) + 1

        return num_of_sums


a = Solution()
print(a.subarraySum([1,1,1], 2))    # 2
print(a.subarraySum([1,2,3], 3))    # 2
print(a.subarraySum([1], 0))    # 0