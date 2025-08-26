class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_dia, max_area = 0, 0
        for l, w in dimensions:
            dia = (l * l) + (w * w)
            if dia > max_dia:
                max_dia = dia
                max_area = l*w

            elif dia == max_dia:
                max_area = max(max_area, l*w)
                
        return max_area
    

a = Solution()
print(a.areaOfMaxDiagonal([[5, 4], [3, 2], [4, 6]]))  # Output: 24
print(a.areaOfMaxDiagonal([[2, 3], [1, 4]]))          # Output: 6