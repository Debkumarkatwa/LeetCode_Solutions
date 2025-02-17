class Solution(object):
    def isPalindrome(self, x):
        a=str(x)
        a=a[::-1]
        if a==str(x):
            return True
        else:
            return False
        