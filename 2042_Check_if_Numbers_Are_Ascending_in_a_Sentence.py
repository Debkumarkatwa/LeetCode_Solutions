class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(' ')
        nums = []
        for i in s:
            if i.isdigit():
                nums.append(int(i))
                if len(nums) > 1:
                    if nums[-1] <= nums[-2]:
                        return False
        return True


a = Solution()
print(a.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))