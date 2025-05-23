class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        a, degree = set(nums), 0
        for num in a:
            degree = max(nums.count(num), degree)

        result, count = len(nums), {}
        for index, value in enumerate( nums):
            count[value] = count.get(value, 0) + 1
            
            if count[value] == degree:
                start = nums.index(value)
                a = index - start + 1

                result = a if a < result else result
                   
        return result
    
# Example usage
a = Solution()
print(a.findShortestSubArray([1,2,2,3,1]))  # Output: 2
print(a.findShortestSubArray([1,2,2,3,1,4,2]))  # Output: 6
print(a.findShortestSubArray([2,1,1,2,1,3,3,3,1,3,1,3,2]))  # Output: 7