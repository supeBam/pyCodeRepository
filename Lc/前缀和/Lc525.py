import collections
from typing import List


class Solution:
    '''
    找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
    [0,1,1,1,1,1,0,0,0]   n = 9

   0[-1,0,1,2,3,4,3,2,1]

    '''

    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # key：前缀和  value：下标索引
        # 遇到 0 则 -1， 遇到 1 则 +1
        # 当字典中含有相同的 前缀和， 则代表 1 和 0 个数相同
        # 如果 s[r] 和 s[r2]相等,  则 s[r2] - s[r] = s[r] - s[l]
        d = dict()
        d[0] = -1
        cur = 0
        for i in range(n):
            k = nums[i]
            if k == 0:
                cur -= 1
            else:
                cur += 1
            # 有相同的值, 则找到区间
            if cur in d:
                ans = max(ans, i - d[cur])
            else:
                d[cur] = i

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]))
