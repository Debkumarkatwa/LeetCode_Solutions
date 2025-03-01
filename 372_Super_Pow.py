class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        c = ''.join(str(i) for i in b)
        return(pow(a,int(c),1337))

a = Solution()
print(a.superPow(2,[3])) 
print(a.superPow(2,[1,0])) 
print(a.superPow(2,[4,3,3,8,5,2])) 
print(a.superPow(2,[0])) 