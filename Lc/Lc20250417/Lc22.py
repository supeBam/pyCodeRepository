from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 生成 n 对 括号
        m = 2 * n
        ans = []
        path = [''] * m

        def dfs(i: int, open: int):
            # 返回条件
            if i == m:
                ans.append(''.join(path))
                return

            # 当左括号个数 < n 时
            if open < n:
                # 选左括号
                path[i] = '('
                dfs(i + 1, open + 1)

            # 当右括号个数 < 左括号时
            if open > i - open:
                path[i] = ')'
                dfs(i + 1, open)

        dfs(0, 0)
        return ans

main = Solution()
ans = main.generateParenthesis(3)
print(ans)