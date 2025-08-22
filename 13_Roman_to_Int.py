class Solution:
    def romanToInt(self, s: str) -> int:
        b, result, flag = [], 0, 0 
        
        for i in s:
            match i:
                case "I":
                    b.append(1)
                case "V":
                    b.append(5)
                case "X":
                    b.append(10)
                case "L":
                    b.append(50)
                case "C":
                    b.append(100)
                case "D":
                    b.append(500)
                case "M":
                    b.append(1000)

        
        for i in range(len(b)):
            if flag == 1:
                flag = 0
                continue
            
            if i == len(b)-1:   result +=b[i]
            
            else:
                if b[i] < b[i+1]:
                    result += (b[i+1]-b[i])
                    flag = 1
                else:
                    result += b[i]
        
        return result
    

a = Solution()
print(a.romanToInt("III")) # 3
print(a.romanToInt("IV")) # 4
print(a.romanToInt("IX")) # 9
print(a.romanToInt("LVIII")) # 58