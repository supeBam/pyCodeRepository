from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        flag = [False] * n
        path = []

        def dfs(deep: int, path: List[int], flag: List[bool]) -> None:
            if n == len(path):
                ans.append(path.copy())
                return
            for i, v in enumerate(nums):
                # 选过标识, 枚举
                if flag[i]:
                    continue
                # 没选过 则选
                path.append(v)
                flag[i] = True

                dfs(deep + 1, path, flag)

                flag[i] = False
                path.pop()

        dfs(0, path, flag)
        return ans

main = Solution()
ans = main.permute([1, 2, 3])
print(ans)