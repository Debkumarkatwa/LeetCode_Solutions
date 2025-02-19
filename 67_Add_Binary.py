# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         a = int(a, 2)
#         b = int(b, 2)
#         return bin(a + b)[2:]
    
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = (int(a, 2) + int(b, 2)), ""
        if a == 0:
            return "0"
        while a > 0:
            a, c = a // 2, a % 2
            b = str(c) + b
        return b
        



a = Solution()
print(a.addBinary("11", "1"))
print(a.addBinary("1010", "1011"))
print(a.addBinary("0", "0"))