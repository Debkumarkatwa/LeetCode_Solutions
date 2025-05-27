class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_array = sorted(arr)
        libary = {}

        for i in sorted_array:
            if i not in libary:
                libary[i] = len(libary) + 1

        for index, value in enumerate(arr):
            sorted_array[index] = libary[value]

        return sorted_array
    
# Example usage
a = Solution()
print(a.arrayRankTransform([40, 10, 20, 30]))  # Output: [4, 1, 2, 3]
print(a.arrayRankTransform([100, 100, 100]))  # Output: [1, 1, 1]
print(a.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))  # Output: [5, 3, 4, 2, 8, 6, 7, 1, 3]