from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        numbers = []
        for operation in operations:
            if operation == '+':
                numbers.append(numbers[-1] + numbers[-2])
            elif operation == 'D':
                numbers.append(numbers[-1] * 2)
            elif operation == 'C':
                numbers.remove(numbers[-1])
            else:
                numbers.append(int(operation))
        return sum(numbers)


if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
