from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        a = set(permutations(digits, 3))
        b = [int(''.join(map(str, i))) for i in a if (i[0] > 0 and i[-1] % 2 == 0 )]
        
        return(sorted(b))
    
# Example usage
a = Solution()
print(a.findEvenNumbers([2,1,3,0]))  # Output: [102,120,130,132,210,230,302,310,312,320]
print(a.findEvenNumbers([2,2,8,8,2]))  # Output: [222,228,282,288,822,828,882]