class Solution:
    def fib(self, N: int) -> int:
        
        beg = 1
        fib1 = 0
        fib2 = 0
        fib3 = 0
        
        if N == 0:
            return 0
        else:
            for x in range(N):
                fib3 = fib2
                fib2 = fib1
                fib1 = fib2 + fib3 + beg
                beg = 0

            
        return fib1
