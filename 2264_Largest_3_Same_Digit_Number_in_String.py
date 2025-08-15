class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ''
        count = 1

        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                count += 1
            else:
                count = 1

            if count == 3:
                if result != '' and int(num[i] * 3) > int(result):
                    result = num[i-2:i+1]

                if result == '':
                    result = num[i-2:i+1]
                

        return result


a = Solution()
print(a.largestGoodInteger("6777133339"))  # Output: "777"
print(a.largestGoodInteger("2300019"))     # Output: "000"
print(a.largestGoodInteger("42352338"))    # Output: ""