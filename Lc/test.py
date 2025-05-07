from collections import Counter
from email.charset import Charset

numRows = 5
c = [[1] * (i + 1) for i in range(numRows)]

print(c)

f = [1] + [0] * 3 +[2]
print(f)

ans = [1,3,2,3,3,6,7,8,6,6,6]

print(max(ans))
print(ans.count(max(ans)))

def count_unique_substrings(s: str) -> int:
    n = len(s)
    seen = set()
    left = 0
    res = 0

    for right in range(n):
        while s[right] in seen:  # 如果当前字符已存在，收缩窗口
            seen.remove(s[left])
            left += 1
        seen.add(s[right])  # 加入当前字符
        res += right - left + 1  # 新增的子串数
    return res

print(count_unique_substrings('abcabcbb'))

power = [1, 1, 3, 4]
cnt = Counter(power)
a = sorted(cnt.keys())
print(cnt)
print(a)

memo = {}
memo[1] = 1
print(memo.get(1, 0))
print(memo.get(2, 0))

print(ord("a"))
print(type(ord("a")))
