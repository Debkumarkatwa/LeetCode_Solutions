class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        a, b = [], []
        for i in nums:
            if i < pivot:
                a.append(i)
            if i > pivot:
                b.append(i)
        
        a.extend([pivot for i in range(len(nums)-len(a)-len(b))])
        a.extend(b)

        return a
                     
                        

a = Solution()
print(a.pivotArray([9,12,5,10,14,3,10],10))
print(a.pivotArray([-3,4,3,2],2))