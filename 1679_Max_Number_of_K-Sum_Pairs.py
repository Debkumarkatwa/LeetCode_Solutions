class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = 0
        num_count = {}

        for num in nums:
            complement = k - num
            if complement in num_count and num_count[complement] > 0:
                count += 1
                num_count[complement] -= 1
            else:
                if num not in num_count:
                    num_count[num] = 0
                num_count[num] += 1

        return count
        


a = Solution()
print(a.maxOperations([1, 2, 3, 4], 5))  # Output: 2
print(a.maxOperations([3, 1, 3, 4, 3], 6))  # Output: 1