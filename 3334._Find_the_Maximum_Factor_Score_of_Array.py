import math
from functools import reduce

class Solution:
    def maxScore(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0] * nums[0]
        if len(nums) == 0:
            return 0

        max_score = reduce(math.lcm, nums) * reduce(math.gcd, nums)
        lcm = gcd = 1

        for i in range(len(nums)):
            lcm = reduce(math.lcm, nums[:i] + nums[i+1:])
            gcd = reduce(math.gcd, nums[:i] + nums[i+1:])
        
            if lcm * gcd > max_score:
                max_score = lcm * gcd
                
        return max_score

# Example usage
a = Solution()
print(a.maxScore([0]))  # Output: 1