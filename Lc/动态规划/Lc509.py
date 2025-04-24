class Solution:
    '''
    转移方程: f(n) = f(n-1) + f(n-2)
    '''
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a = 0
        b = 1
        for i in range(2, n + 1):
            a, b = b, a + b

        return b