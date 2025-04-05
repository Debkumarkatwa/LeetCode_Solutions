class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]: 
        n = len(code)
        if k == 0:    return [0] * n
        
        code = code + code
        if k > 0:
            for i in range(n):
                code[i] = sum(code[i+1:i+k+1])
        
        else:
            for i in range(n):
                code[i] = sum(code[i+n+k:i+n])

        return code[:n]
        
        
a = Solution()
print(a.decrypt(code = [5,7,1,4], k = 3))   # [12,10,16,13]
print(a.decrypt(code = [1,2,3,4], k = 0))   # [0,0,0,0]
print(a.decrypt(code = [2,4,9,3], k = -2))  # [12,5,6,13]