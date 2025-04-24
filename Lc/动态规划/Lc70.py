class Solution:
    def climbStairs(self, n: int) -> int:

        '''
        定义 最优子结构    f(n - 1), f(n - 2)
        转移方程:   f(n) = f(n-1) + f(n-2)
        重叠子问题：  f(10) = f(9) + f(8)   f(9) = f(8) + f(7) ... 有重复
        '''
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        # 走到 n 的个数
        for i in range(3, n + 1):
            a, b = b, a + b

        return b