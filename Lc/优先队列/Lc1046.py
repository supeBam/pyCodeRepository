import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones) > 1:
            max_1 = heapq.heappop()
            max_2 = heapq.heappop()
            if max_1 == max_2:
                continue
            else:
                heapq.heappush(stones, abs(max_1 - max_2))

        return stones[0] if stones else 0

if __name__ == '__main__':
    s = Solution()
    print(s.lastStoneWeight([10,4,2,10]))