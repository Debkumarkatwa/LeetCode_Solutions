class Solution:
    def maximum69Number (self, num: int) :
        a = list(str(num))

        for index, value in enumerate(a):
            if value == '6':
                a[index] = '9'
                break
    
        return int(''.join(a))
        


a = Solution()
print(a.maximum69Number(9669))  # Output: 9969
print(a.maximum69Number(9999))  # Output: 9999
print(a.maximum69Number(9996))  # Output: 9999
print(a.maximum69Number(6666))  # Output: 9666