import this


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        n1 = list(s1)
        n2 = list(s2)
        print(n1, end='\n')
        print(n2, end='\n')
        n1.sort()
        n2.sort()

        # 因为 None == None 为True
        print(n1.sort() == n2.sort(), end='\n')

        print(n1, end='\n')
        print(n2, end='\n')

        print(n1 == n2)
        for i in range(len(n1)):
            if n1[i] != n2[i]:
                return False
        return True


if __name__ == '__main__':
    a = Solution()
    a.CheckPermutation("abc", "bad")
