from typing import List


class Solution:
    '''
    转移方程:   f(n) = f(n >> 1) + (i & 1)
    '''

    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # i % 2 和 i & 1 都可以用来判断最低位是否为1
            # 从高位向低位移动，利用之前计算过的 1 个数，最后判断 最低位是否为1
            dp[i] = dp[i >> 1] + (i & 1)

        return dp

if __name__ == '__main__':
    s = Solution()
    print(s.countBits(8))