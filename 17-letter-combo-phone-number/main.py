from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        self.map = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
        }

        def backtrack(index, path):

            if index == len(digits):
                self.res.append(path)
                return

            for each in self.map[digits[index]]:
                backtrack(index + 1, path + each)

        backtrack(0, "")
        return self.res


sol = Solution()

print(sol.letterCombinations("23"))
        
