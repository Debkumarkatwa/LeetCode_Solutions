class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 2
        while i < len(s):
            if s[i] == s[i-1] == s[i-2]:
                s = s[:i] + s[i+1:]
            else:
                i += 1

        return s
    

a = Solution()
print(a.makeFancyString("leeetcode"))  # "leetcode"
print(a.makeFancyString("aaabaaaa"))  # "aabaa"
print(a.makeFancyString("aab"))  # "aab"
print(a.makeFancyString("a"))  # "a"
print(a.makeFancyString("aaa"))  # "aa"