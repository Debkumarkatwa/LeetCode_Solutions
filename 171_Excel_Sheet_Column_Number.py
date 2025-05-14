class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber > 0:
            columnNumber -= 1
            ans = chr(columnNumber % 26 + 65) + ans
            columnNumber //= 26

        return ans

# Example usage
a = Solution()
print(a.convertToTitle(701))  # Output: 701