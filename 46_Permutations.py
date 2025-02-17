from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(set(permutations(nums)))  # set() is faster than list() & loop for removing duplicates
    