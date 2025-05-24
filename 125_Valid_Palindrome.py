class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_chars = [c.lower() for c in s if c.isalpha() or c.isdigit()]
        
        # Check if the filtered characters form a palindrome
        return filtered_chars == filtered_chars[::-1]
    
# Example usage:
a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))     # True
print(a.isPalindrome("race a car"))     # False
print(a.isPalindrome(" . "))     # True