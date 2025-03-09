class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        a = []
        for i in range(len(s) - k + 1):
            b = s[i:i+k].count('a') + s[i:i+k].count('e') + s[i:i+k].count('i') + s[i:i+k].count('o') + s[i:i+k].count('u')
            a.append(b)
        return max(a)
    

a = Solution()
print(a.maxVowels(s = "abciiidef", k = 3))  # 3
print(a.maxVowels(s = "aeiou", k = 2))  # 2
print(a.maxVowels(s = "leetcode", k = 3))  # 2