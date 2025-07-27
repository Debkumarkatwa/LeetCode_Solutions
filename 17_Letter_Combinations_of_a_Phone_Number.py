from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        MAP = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        if not digits:
            return []
        result = product(*(MAP[digit] for digit in digits))
        print(result)

        return [''.join(combination) for combination in result]


a = Solution()
print(a.letterCombinations("23")) # Expected output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(a.letterCombinations("")) # Expected output: []
print(a.letterCombinations("2")) # Expected output: ["a", "b", "c"]