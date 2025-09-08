class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse= 1)
        SUM, result = sum(nums), []

        for i in nums:
            result.append(i)
            SUM -= i
            if sum(result) > SUM:
                return result


a = Solution()
print(a.minSubsequence([4,3,10,9,8]))       # [10, 9]
print(a.minSubsequence([4,4,7,6,7]))        # [7, 7, 6]