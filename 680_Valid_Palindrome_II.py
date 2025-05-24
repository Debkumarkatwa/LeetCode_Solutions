class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                '''
                Check by skipping either the left or the right character
                we don't need to check it multiple time as we can only remove one character
                '''
                skip_left = s[left + 1:right + 1] == s[left + 1:right + 1][::-1]
                skip_right = s[left:right] == s[left:right][::-1]
                return skip_left or skip_right
            
            left += 1
            right -= 1

        return True

# Example usage:
a = Solution()
print(a.validPalindrome("aba"))     # True
print(a.validPalindrome("abca"))     # True (remove 'b' or 'c')
print(a.validPalindrome("abc"))     # False (cannot be made a palindrome)