class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence = sentence.split(' ')
        for j,i in enumerate(sentence):
            if '$' in i:
                try:
                    i = str(int(i[1:]) * (100 - discount) / 100).split('.') # to verify the decimal point is 2
                    if len(i[1]) < 2:
                        sentence[j] = '$' + '.'.join(i) + '0'
                    else:
                        sentence[j] = '$' + i[0] + '.' + i[1][:2]  
                except:
                    pass

        return ' '.join(sentence)






a = Solution()
print(a.discountPrices("there are $1 $2 and 5$ candies in the shop", 50))
print(a.discountPrices("1 2 $3 4 $5 $6 7 8$ $9 $10$", 100))
