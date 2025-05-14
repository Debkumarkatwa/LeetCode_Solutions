class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        # return arr.index(max(arr))
        
        for i in range(1, len(arr)-1):
            if( (arr[i] > arr[i-1]) and (arr[i] > arr[i+1]) ):
                return i
    
# Example usage
a = Solution()
print(a.peakIndexInMountainArray([5,4,8,7,10,2]))  # Output: 6
print(a.peakIndexInMountainArray([8,6,1,5,3]))  # Output: 9
print(a.peakIndexInMountainArray([1,2,3,4,5]))  # Output: 4