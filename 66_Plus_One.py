class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = 0
        for i in digits:    
            a = a * 10 + i

        a += 1
        digits = []
        
        for i in str(a):    
            digits.append(int(i))
        return digits

a = Solution()
print(a.plusOne([1, 2, 3]))
print(a.plusOne([4, 3, 2, 1]))
print(a.plusOne([0]))
print(a.plusOne([99]))
print(a.plusOne([109]))
