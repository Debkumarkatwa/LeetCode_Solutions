class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:    return True
        if not t:    return False
        
        s_index, t_index = 0, 0
        while t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            if s_index == len(s):
                return True
            t_index += 1
            
        return False
        
# Example usage:
a = Solution()
print(a.isSubsequence("abc", "ahbgdc"))  # Output: True
print(a.isSubsequence("axc", "ahbgdc"))  # Output: False
print(a.isSubsequence("", "ahbgdc"))     # Output: True
print(a.isSubsequence("aec", "abcde"))   # Output: False