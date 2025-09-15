class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        words = text.split()
        count = 0
        
        for word in words:
            word_set = set(word)
            if word_set.isdisjoint(broken_set):                   #if not (word_set & broken):
                count += 1
                
        return count


a = Solution()
print(a.canBeTypedWords("hello world", "ad"))  # Output: 1
print(a.canBeTypedWords("leet code", "lt"))  # Output: 1
print(a.canBeTypedWords("leet code", "e"))  # Output: 0
