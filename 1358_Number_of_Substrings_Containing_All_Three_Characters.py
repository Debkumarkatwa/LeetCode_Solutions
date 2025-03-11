class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        list_, Count = [], 0

        for i in range( len(s[:-2]) + 1 ):
            if s[i] == 'a' and 'b' in s[i:] and 'c' in s[i:]:
                list_.append(['a', max(i+s[i:].index('b'), i+s[i:].index('c'))])

            elif s[i] == 'b' and 'a' in s[i:] and 'c' in s[i:]:
                list_.append(['b', max(i+s[i:].index('a'), i+s[i:].index('c'))])

            elif s[i] == 'c' and 'a' in s[i:] and 'b' in s[i:]:
                list_.append(['c', max(i+s[i:].index('a'), i+s[i:].index('b'))])

        for i in list_:
            Count = Count + (len(s) - i[1])
        return (Count)


a = Solution()
print(a.numberOfSubstrings("abcabc")) #10
print(a.numberOfSubstrings("aaacb")) #3
print(a.numberOfSubstrings("abc")) #1