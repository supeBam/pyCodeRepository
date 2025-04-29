class Solution:
    def punishmentNumber(self, n: int) -> int:

        def dfs(curPot: int, numStr: str, total: int, target: int) -> bool:
            # 边界
            if curPot == len(numStr):
                return  total == target

            sums = 0
            for i in range(curPot, len(numStr)):
                # 当前元素
                sums = sums * 10 + int(numStr[i])
                # 超出目标值，直接剪枝
                if sums + total > target:
                    break
                if dfs(i + 1, numStr, sums + total, target):
                    return True

            return False

        ans = 0
        for i in range(1, n + 1):
            if dfs(0, str(i * i), 0, i):
                ans += i * i
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.punishmentNumber(36))
