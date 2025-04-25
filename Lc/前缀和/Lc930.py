from typing import List


class Solution:
    '''
    [1, 0, 1, 0, 1], goal=2
    '''

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        l1, l2 = 0, 0
        sum1 , sum2 = 0, 0
        ans = 0
        for r in range(n):
            sum1 += nums[r]
            while sum1 > goal:
                sum1 -= nums[l1]
                l1 += 1


            sum2 += nums[r]
            while sum2 >= goal:
                sum2 -= nums[l2]
                l2 += 1

            ans += l2 - l1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarraysWithSum([1, 0, 1, 0, 1], goal=2))
