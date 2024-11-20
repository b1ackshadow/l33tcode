from typing import List
class Solution:

    def __init__(self):
        self.cache = {}
        self.res = []

    def is_palindrome(self, s: str):
        l = 0; h = len(s) - 1;
        while l < h:
            if s[l] != s[h]:
                self.cache[s] = False
                return False
            l += 1
            h -= 1
        self.cache[s] = True
        return True

    def partition(self, s: str) -> List[List[str]]:

        def backtack(start, path):

            if start == len(s):
                self.res.append(path)
                return

            for i in range(start + 1, len(s) + 1):
                l_part = s[start:i]

                if not l_part in self.cache:
                    self.is_palindrome(l_part)
                if self.cache[l_part]:
                    backtack(i, path + [l_part])
        backtack(0, [])
        return self.res


sol = Solution()

res = sol.partition("aaab")
print(res)
