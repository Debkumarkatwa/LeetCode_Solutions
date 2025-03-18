class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        track, count = [], 0
        for index, num in enumerate(nums):
            if num % 2 != 0:
                track.append(index)
        
        track = [-1] + track + [len(nums)]
        
        for i in range(1, len(track) - k):
            count += (track[i] - track[i-1]) * (track[i+k] - track[i+k-1])
        return count
            
            
a = Solution()
print(a.numberOfSubarrays(nums = [1,1,2,1,1], k = 3)) #2
print(a.numberOfSubarrays(nums = [2,4,6], k = 1)) #0
print(a.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2)) #16