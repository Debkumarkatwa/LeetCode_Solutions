from itertools import combinations
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result, a = [], []
        for i in range(len(nums) + 1):
            a.extend(list(combinations(nums, i)))
        
        for i in a:
           result.append(list(i)) 
        return result