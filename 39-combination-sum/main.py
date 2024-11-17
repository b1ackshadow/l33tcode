from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.candidates = candidates
        self.len = len(candidates)
        self.pick(0, target, [])
        return self.result

    def pick(self, index, target, current):

        if target == 0:
            self.result.append(current)
            return

        if index == self.len or target < 0:
            return

        # pick
        self.pick(index, target - self.candidates[index], current + [self.candidates[index]])

        # dont pick
        self.pick(index + 1, target, current)


sol = Solution()

res = sol.combinationSum([2], 1)

print(res)
