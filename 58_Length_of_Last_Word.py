class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(' ')[::-1]
        for i in a:
            if i != '':
                return len(i)
        