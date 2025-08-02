class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-' or x[0] == '+':
            x =x[:0:-1]
            x = int(x)*(-1)
            if (x < (-1)*2**31):
                return 0
            return x
        else:
            x = x[::-1]
            x = int(x)
            if (x > (2**31)-1):
                return 0
            return x
        

a = Solution()
print(a.reverse(123))
print(a.reverse(-123))
print(a.reverse(43))
print(a.reverse(2147483651))