class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        a = {}
        for i in nums1:
            a[i[0]] = i[1]

        for i in nums2:
            if i[0] in a:
                a[i[0]] += i[1]
            else:
                a[i[0]] = i[1]

        a = sorted(a.items())
        return a
            



a = Solution()
print(a.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
print(a.mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))