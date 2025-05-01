class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        a = {}
        result = []
        for i in nums:
            if i not in a.keys():
                a[i] = 0
            a[i] += 1

            if i not in result and a[i] > (len(nums)/3):
                result.append(i)

            if len(result) == 2:
                return result

        return result

        
a = Solution()
print(a.majorityElement([3,2,3]))  # [3]
print(a.majorityElement([1]))  # [1]
print(a.majorityElement([1,2]))  # [1,2]
print(a.majorityElement([1,2,3,4,5,6,7,8,9,10]))  # [1,2,3,4,5,6,7,8,9,10]