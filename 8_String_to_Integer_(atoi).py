class Solution:
    a = "0"
    def myAtoi(self, s: str) -> int:
        for i in range(len(s)):  # remove leading spaces
            if s[i] != " ":
                s = s[i:]
                break

        if s[0] == "+" or s[0] == "-":  # check if first character is a sign
            for i in s[1:]: # if sign is present, check for next character
                if i.isdigit():
                    self.a = self.a + i
                else:
                    break

            self.a = int(self.a)*(int(s[0]+"1"))

        else:
            for i in s:
                if i.isdigit():
                    self.a = self.a + i
                else:
                    break

            self.a = int(self.a)

        if self.a < (-1)*(2**31):
            return (-1)*(2**31)
        elif self.a > (2**31)-1:
            return (2**31)-1
        else:
            return self.a


a=Solution()
print(a.myAtoi("-91283472332"))


