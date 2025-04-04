from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
    
a = Solution()
print(a.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))  # ABC
print(a.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))  # AB
print(a.gcdOfStrings(str1 = "LEET", str2 = "CODE"))  # ""
print(a.gcdOfStrings(str1 = "ABCDEF", str2 = "ABC"))  # ""