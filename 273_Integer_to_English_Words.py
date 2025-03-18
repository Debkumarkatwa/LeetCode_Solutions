class Solution:
    d = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand", # 4,5
        1000000: "Million", # 7,8
        1000000000: "Billion"
        }
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        Co, result = [], []
        for number, word in list(self.d.items())[::-1]:
            c = 0
            while num >= number:
                num -= number
                c += 1

            if c != 0:     
                Co.append([c,number])

        # print(Co)
              
        for x in Co:
            a = []    
            if x[0] == 100:    
                a.append('One Hundred')    
                   
            elif x[0] > 1 or x[1] >= 100:
                if x[0] in self.d.keys():
                    a.append(self.d[x[0]])
                else:
                    a.append(self.numberToWords(x[0]))
            a.append(self.d[x[1]])
            # print(a)
            result.append(' '.join(a))

        return ' '.join(result)
            

a = Solution()
# print(a.numberToWords(1294597)    )  # "One Million Two Hundred Ninety Four Thousand Five Hundred Ninety Seven" 
# print(a.numberToWords(123)        )  # "One Hundred Twenty Three"
# print(a.numberToWords(12345)      )  # "Twelve Thousand Three Hundred Forty Five"
# print(a.numberToWords(1234567)    )  # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
print(a.numberToWords(100000)     )  # "One Hundred Thousand"
# print(a.numberToWords(10000)      )  # "Ten Thousand"
# print(a.numberToWords(9317)       )  # "Nine Thousand Three Hundred Seventeen"
# print(a.numberToWords(1234567891) )  # "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
# print(a.numberToWords(400)        )  # "Four Hundred"
# print(a.numberToWords(178009709020)) # "One Hundred Seventy Eight Billion Nine Million Seven Hundred Nine Thousand Twenty"