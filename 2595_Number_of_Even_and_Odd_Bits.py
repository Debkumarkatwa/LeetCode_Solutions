class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        result = [0, 0]
        n = bin(n)[:1:-1]  # convert n in Binary form and reverse it
        
        for i in range(len(n)):
            if (n[i] == '1') and (i % 2 == 0):
                result[0] += 1
                
            elif n[i] == '1':
                result[1] += 1
                
        return result
        
    
a = Solution()
print(a.evenOddBit(50))  # [1, 2]
print(a.evenOddBit(2))  # [0, 1]