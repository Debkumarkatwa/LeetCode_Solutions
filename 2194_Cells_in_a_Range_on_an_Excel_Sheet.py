class Solution:
    def cellsInRange(self, s: str) -> list[str]:

        start_col, end_col = ord(s[0]), ord(s[3])
        start_row, end_row = int(s[1]), int(s[4])
        result = []

        for coloum in range(start_col, end_col + 1):
            result.extend([f"{chr(coloum)}{row}" for row in range(start_row, end_row + 1)])
        
        return result
        

# Example usage
a = Solution()
print(a.cellsInRange('K1:L2'))  # Output: 701