from sys import flags
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        flag = [False] * n
        path = []
        d = set()

        def dfs(deep, path, flag) -> None:
            if n == len(path) and (frozenset(path) not in d):
                d.add(frozenset(path))
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
ans = main.permuteUnique([1, 1, 2])
print(ans)
