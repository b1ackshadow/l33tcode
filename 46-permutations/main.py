from typing import List, Optional
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.res = []
        self.computePerm(nums, [])
        return self.res

    def computePerm(self, available: List[int], accumulator):
        if len(accumulator) == self.n:
            self.res.append(accumulator)
            return

        if len(available) == 0:
            return

        # try each candidate
        for i, e in enumerate(available):
            accumulator.append(e)
            available.pop(i)
            self.computePerm(available, accumulator[:])
            available.insert(i, e)
            accumulator.pop()

        
        


tests = [
    ([1,2,3], sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])),
    ([0,1],[[0,1],[1,0]])
]

for i, (test, want) in enumerate(tests):

    sol = Solution()
    got = sorted(sol.permute(test))
    print(got)

    # assert got == want, f"Test {i + 1} failed got {got} but wanted {want}"

