class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        a = {}

        for num in nums:
            if num not in a.keys():
                a[num] = 0
            a[num] += 1
        return max(a, key=a.get)

a = Solution()
print(a.majorityElement([2,2,1,1,1,2,2]))  # Output: 2




