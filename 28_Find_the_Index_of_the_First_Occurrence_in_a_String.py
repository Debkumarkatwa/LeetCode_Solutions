class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1




a = Solution()
print(a.strStr("sadbutsad", "d"))
print(a.strStr("leetcode", "leeto"))
print(a.strStr("", "v"))
print(a.strStr("a", "a"))