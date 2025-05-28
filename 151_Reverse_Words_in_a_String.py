class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return ' '.join(reversed(words))

a = Solution()
print(a.reverseWords('the sky is blue'))  
print(a.reverseWords('  hello world  '))  
print(a.reverseWords('a good   example'))  