# sys.set_int_max_str_digits(10000)
# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         return str(int(num1) + int(num2))


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
    
    def int_to_string(self, num):
        if num == 0:
            return "0"
        a = ""
        while num > 0:
            num, b = divmod(num, 10)
            match b:
                case 0:
                    a = "0" + a
                case 1:
                    a = "1" + a
                case 2:
                    a = "2" + a
                case 3:
                    a = "3" + a
                case 4:
                    a = "4" + a
                case 5:
                    a = "5" + a
                case 6:
                    a = "6" + a
                case 7:
                    a = "7" + a
                case 8:
                    a = "8" + a
                case 9:
                    a = "9" + a
        return a
    
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = self.string_to_int(num1)
        num2 = self.string_to_int(num2)
        return self.int_to_string(num1 + num2)