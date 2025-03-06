from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # a = [str(i) for i in range(1, n+1)] 
        # b = list(permutations(a)) 
        # return ''.join(b[k-1])
        
        return ''.join(list(permutations([str(i) for i in range(1, n+1)]))[k-1])
        

a = Solution()
print(a.getPermutation(3, 3))    # "213"
print(a.getPermutation(4, 9))    # "2314"
print(a.getPermutation(3, 1))    # "123"
print(a.getPermutation(3, 2))    # "132"