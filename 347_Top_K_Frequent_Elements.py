class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        store = dict()

        for i in nums:
            store[i] = store.get(i, 0) + 1

        store = dict(sorted(store.items(), key=lambda item: item[1], reverse=True))

        return list(store.keys())[:k]

# Example usage:
solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # Output: [1, 2]
print(solution.topKFrequent([1], 1))  # Output: [1]
print(solution.topKFrequent([1, 2], 2))  # Output: [1, 2]