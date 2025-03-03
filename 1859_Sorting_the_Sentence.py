class Solution:
    def sortSentence(self, s: str) -> str:
        a =[]
        s = s.split(' ')
        for i in range(len(s)):
            a.append(' ')
        # you can also use this instead of the above for loop
        # a = ['','','','','','','','','']   # as the maximum length of s is 9
        for i in s:
            a[int(i[-1])-1] = i[0:-1]
        return ' '.join(a)
        


a = Solution()
print(a.sortSentence("is2 sentence4 This1 a3")) # "This is a sentence"