class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = [ 0 * [] for i in range(len(matrix)) ]
        for i in range(len(r)):
            for j in matrix[::-1]:
                r[i].append(j[i])
        
        for i in range(len(r)):
            matrix[i] = r[i]

        # print(matrix)
        

a = Solution()
a.rotate([[1,2,3],[4,5,6],[7,8,9]]) # [[7,4,1],[8,5,2],[9,6,3]]
