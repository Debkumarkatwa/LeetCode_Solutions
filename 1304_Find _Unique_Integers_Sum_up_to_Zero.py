class Solution:
    def sumZero(self, n: int) -> list[int]:
        result = []
        for num in range( 1, (n // 2)+1 ):
            result.extend([(-1 * num), num])

        if n % 2 != 0:
            result.append(0)
        
        return result
    

a = Solution()
print(a.sumZero(5))     # [-2, -1, 0, 1, 2]
print(a.sumZero(3))     # [-1, 0, 1]
