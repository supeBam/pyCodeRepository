from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        def backtrack( i: int, path: List[int]):
            if i == n:
                ans.append(path.copy())
                return

#           # 不选
            backtrack(i + 1, path)

            # 选
            path.append(nums[i])
            backtrack(i + 1, path)

            # 还原
            path.pop()

        backtrack(0, path)
        return ans


