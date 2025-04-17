from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        answer = []
        path  = [""] * n
        def dfs(index: int):
            if index == n:
                answer.append("".join(path))
                return

            for c in dict[digits[index]]:
                path[index] = c
                dfs(index + 1)

        dfs(0)
        return answer



