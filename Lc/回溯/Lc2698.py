class Solution:
    def punishmentNumber(self, n: int) -> int:

        nums = [str(i) for i in str(n)]
        ans = []
        path = []

        def dfs(deep):
            if deep == len(nums) and sum(nums) == s:
                ans.append(path.copy())
                return

            for i in range(deep, len(nums)):
                path.append(''.join(nums[deep: i + 1]))
                dfs(i + 1)
                path.pop()

        dfs(0)
        return len(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.punishmentNumber(1))
