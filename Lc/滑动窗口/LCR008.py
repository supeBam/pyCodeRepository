from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 1_000_00
        res = 0
        l = 0
        for r in range(len(nums)):
            res += nums[r]
            # 移动左指针
            while res >= target:
                ans = min(ans, r - l + 1)
                res -= nums[l]
                l += 1

        return ans if ans != 1_000_00 else 0
if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(s.minSubArrayLen(4, [1,4,4]))
    print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))
    print(s.minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))
