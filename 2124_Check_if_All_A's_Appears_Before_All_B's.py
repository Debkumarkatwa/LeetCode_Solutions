class Solution:
    def checkString(self, s: str) -> bool:
        a = 0
        for i in s:
            if a == 1 and i == 'a':
                return False
            if i == 'b':
                a = 1
        return True
            

a = Solution()
print(a.checkString("ab")) # True
print(a.checkString("aba")) # False