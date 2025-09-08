class Solution:
    def findLucky(self, arr: list[int]) -> int:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        lucky_numbers = [num for num, freq in count.items() if num == freq]
        
        return max(lucky_numbers) if lucky_numbers else -1
            


a = Solution()
print(a.findLucky([2, 2, 3, 4]))  # Output: -1
print(a.findLucky([1, 2, 2, 3, 3, 3]))  # Output: 3
print(a.findLucky([2, 2, 2, 3, 3]))  # Output: -1