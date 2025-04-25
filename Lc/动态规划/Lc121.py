from typing import List


class Solution:
    # 买卖股票的最佳时机
    def maxProfit(self, prices: List[int]) -> int:
        '''
        f(n) 代表 在 n 天时的 最大利润，  当天最大利润 = prices[n](当天价格) - minPrice(最小买入价格)
        定义状态： minPrice = prices[0]
        状态转移：卖 f(n) = max(f(n - 1), prices[n] - minPrice)
        '''
        dp = [0] * len(prices)
        minPrice = prices[0]
        for i in range(1, len(prices)):
            # 不卖, 更新最低价格买入
            minPrice = min(minPrice, prices[i])
            # 卖
            dp[i] = max(dp[i - 1], prices[i] - minPrice)

        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
