class Solution:
    d = {1000:'M',
         900:'CM', 
         500:'D', 
         400:'CD',
         100:'C',
         90:'XC', 
         50:'L', 
         40:'XL',
         10:'X',
         9:'IX',
         5:'V',
         4:'IV', 
         1:'I'
        }
    def intToRoman(self, num: int) -> str:
        roman = ''
        for val, s in self.d.items():
            '''
            if num >= 1000:
                roman += self.d[1000]
                num -= 1000
            elif num >= 900:
                roman += self.d[900]
                num -= 900
            elif num >= 500:
                roman += self.d[500]
                num -= 500
            elif num >= 400:
                roman += self.d[400]
                num -= 400
            elif num >= 100:
                roman += self.d[100]
                num -= 100
            elif num >= 90:
                roman += self.d[90]
                num -= 90
            elif num >= 50:
                roman += self.d[50]
                num -= 50
            elif num >= 40:
                roman += self.d[40]
                num -= 40
            elif num >= 10:
                roman += self.d[10]
                num -= 10
            elif num >= 9:
                roman += self.d[9]
                num -= 9
            elif num >= 5:
                roman += self.d[5]
                num -= 5
            elif num >= 4:
                roman += self.d[4]
                num -= 4
            elif num >= 1:
                roman += self.d[1]
                num -= 1
            '''
            # this is same as above code but more optimized(less code)
            while num >= val:
                roman += s
                num -= val

        return roman
        
        
a = Solution()
print(a.intToRoman(3749)) # MMMMDCCXLIX
print(a.intToRoman(58)) # LVIII
print(a.intToRoman(1994)) # MCMXCIV
print(a.intToRoman(9)) # IX
print(a.intToRoman(4)) # IV
# print(a.intToRoman(int (input("Enter a number: ")) ))