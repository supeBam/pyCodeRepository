from typing import List

'''
f(n) 代表当前最大的值
'''


class Solution:

    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[n - 1] = questions[n - 1][0]
        for i in range(n - 2, -1, -1):
            # 不选 和 选  取当前最大的值
            if i + questions[i][1] + 1 >= n:
                dp[i] = max(dp[i + 1], questions[i][0])
            else:
                dp[i] = max(dp[i + 1], questions[i][0] + dp[i + questions[i][1] + 1])

        return dp[0]

    # 优化1：优雅代码
    def mostPoints2(self, questions: List[List[int]]) -> int:
        n = len(questions)
        # 多增加一个 用于 超出范围的索引值，超出范围 + 0，其实就是取自己
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            # 不选 和 选  取当前最大的值
            dp[i] = max(dp[i + 1], questions[i][0] + dp[min(i + questions[i][1] + 1, n)])

        return dp[0]


if __name__ == '__main__':
    s = Solution()
    print(s.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]))
    print(s.mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
    print(s.mostPoints([[21, 5], [92, 3], [74, 2], [39, 4], [58, 2], [5, 5], [49, 4], [65, 3]]))
