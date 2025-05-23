from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        nums.sort()
        def backtrack(deep, path):

            ans.append(path.copy())

            # 子集问题
            for i in range(deep, len(nums)):

                # 跳过重复元素收集
                if i > deep and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, path)
        return ans



    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(deep, path):
            if deep == len(nums):
                ans.append(path.copy())
                return

            x = nums[deep]
            # 选
            path.append(x)
            backtrack(deep + 1, path)
            path.pop()

            # 不选
            deep += 1
            while deep < len(nums) and x == nums[deep]:
                deep += 1
            backtrack(deep, path)

        backtrack(0, [])
        return ans





if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))