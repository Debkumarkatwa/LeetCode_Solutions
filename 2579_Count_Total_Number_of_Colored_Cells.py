class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 0:    
            return 0

        a = 1
        for i in range(n):
            a += 4*i

        return a



a = Solution()
print(a.coloredCells(1))    # 1
print(a.coloredCells(2))    # 5 (1+4)
print(a.coloredCells(3))    # 13 (1+4+8)
print(a.coloredCells(4))    # 25 (1+4+8+12)
print(a.coloredCells(5))    # 41 (1+4+8+12+16)
print(a.coloredCells(6))    # 61 (1+4+8+12+16+20)