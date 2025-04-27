class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(" ")
        sentence.append(sentence[0])
        
        for index, value in enumerate(sentence[:-1]):
            if value[-1] != sentence[index+1][0]:
                return False
        else:
            return True


a = Solution()
print(a.isCircularSentence("leetcode exercises sound delightful"))    # True
print(a.isCircularSentence("eetcode"))    # True
print(a.isCircularSentence("leetcode eats soul"))   # True
print(a.isCircularSentence("Leetcode is cool"))    # False
print(a.isCircularSentence("I like Leetcode"))    # False
print(a.isCircularSentence("Happy Leetcode"))    # False