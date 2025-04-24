class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        a = 0
        b = 1
        c = 1
        for i in range(2, n + 1):
            a, b, c = b, c, a + b + c

        return c
