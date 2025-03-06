class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:        
        for i in grid[1:]:
            grid[0].extend(i)
        grid[1] = [0,0]

        for i in range(1,len(grid[0])+1):
            if i not in grid[0]:
                grid[1][1] = i
            elif i not in grid[1] and grid[0].count(i) == 2:
                grid[1][0] = i

        return grid[1]


a = Solution()
print(a.findMissingAndRepeatedValues([[1,3],[2,2]]))  # [2, 3]
print(a.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))  # [9, 5]