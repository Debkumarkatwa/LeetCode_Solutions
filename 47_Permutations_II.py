from itertools import permutations
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        return list(set(permutations(nums)))


# its complitly same as 46_Permutations.py  as  46 is allowed to have duplicates but 47 is not allowed to have duplicates 