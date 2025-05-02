class Solution:
    def fib(self, n: int) -> int:
        first, second = 0, 1

        if n == 0:
            return first
        
        elif n == 1:
            return second
        
        else:
            for i in range(2,n+1):
                if i % 2 == 0:
                    first = first + second
                else:
                    second = first +second

        return second if n % 2 != 0 else first
           

a = Solution()
print(a.fib(6))  # Output: 2