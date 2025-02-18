# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         return str(int(num1) * int(num2))


class Solution:
    def string_to_int(self, num):
        a = 0
        for i in num:      
            match i:
                case '0':
                    a = a * 10 + 0
                case '1':
                    a = a * 10 + 1
                case '2':
                    a = a * 10 + 2
                case '3':
                    a = a * 10 + 3
                case '4':
                    a = a * 10 + 4
                case '5':
                    a = a * 10 + 5
                case '6':
                    a = a * 10 + 6
                case '7':
                    a = a * 10 + 7
                case '8':
                    a = a * 10 + 8
                case '9':
                    a = a * 10 + 9
        return a
    
    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.string_to_int(num1)
        num2 = self.string_to_int(num2)
        return str(num1 * num2)


a = Solution()
print(a.multiply("2", "3"))
print(a.multiply("123", "456"))