from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                l = j + 1
                r = n - 1
                k = j
                while l <= r:
                    mid = l + (r - l) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        l = mid + 1
                        k = mid
                    else:
                        r = mid - 1
                ans += k - j
        return ans