from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []

        def dfs(i: int, path: List[int]):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(n):
                path.append(nums[j])
                dfs(j + 1, path)
                path.pop()

        dfs(0, path)
        return ans
