from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def dfs(i, path, ans):
            if i == len(s):
                ans.append(''.join(path))
                return
            # 不选
            dfs(i + 1, path, ans)

            # 选
            if s[i].isalpha():
                # 字母转换
                path[i] = path[i].upper() if path[i].islower() else path[i].lower()

                dfs(i + 1, path, ans)

                # 还原
                path[i] = path[i].upper() if path[i].islower() else path[i].lower()

        ans = []
        dfs(0, list(s), ans)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation("a1b2"))
