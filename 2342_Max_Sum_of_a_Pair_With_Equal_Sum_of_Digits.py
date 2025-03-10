class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        b, max_sum = {}, 0
        for i in nums:
            a = sum(map(int, str(i)))
            if a in b.keys():
                b[a].append(i)
                b[a].remove(min(b[a]))
            else:
                b[a] = [0, i]

        if len(b) == len(nums):
            return -1
        
        for i in b:
            if (0 not in b[i]) and (sum(b[i]) > max_sum):
                max_sum = sum(b[i])
        return max_sum

a = Solution()
print(a.maximumSum([18,43,36,13,7])) # 54
print(a.maximumSum([10,12,19,14,11])) # -1
print(a.maximumSum([9,2,2,5])) # 4
