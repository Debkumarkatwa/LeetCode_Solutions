class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        for i in grid[1:]:
            grid[0].extend(i)
        grid[0].sort()

        neg_count = 0
        for i in grid[0]:
            if i >= 0:
                break
            neg_count += 1
            
        return neg_count
        

a = Solution()
print(a.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])) # 8
print(a.countNegatives(grid = [[3,2],[1,0]])) # 0
print(a.countNegatives(grid = [[1,-1],[-1,-1]])) # 3
print(a.countNegatives(grid = [[-1]])) # 1
print(a.countNegatives(grid = [[1,2,3,4]])) # 0