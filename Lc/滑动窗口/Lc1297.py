from collections import Counter, defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        cnt = Counter()
        cnt2 = Counter()
        l = 0

        for r, c in enumerate(s):
            cnt[c] += 1
            while len(cnt) > maxLetters or r - l + 1 > minSize:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1

            if len(cnt) <= maxLetters and r - l + 1 == minSize:
                cnt2[s[l:r + 1]] += 1

        return max(cnt2.values()) if cnt2 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.maxFreq("aababcaab", maxLetters=2, minSize=3, maxSize=4))
    print(s.maxFreq("aaaa", maxLetters=1, minSize=3, maxSize=3))
    print(s.maxFreq("aabcabcab", maxLetters=2, minSize=2, maxSize=3))

    print(s.maxFreq("abcde", maxLetters=2, minSize=3, maxSize=3))

    # c = Counter()
    # print(c.values())
    # print(len(c))
