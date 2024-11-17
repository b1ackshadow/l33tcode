from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()

        def backtrack(index, current_sum,  subset):
            if index >= len(candidates):
                return

            current_sum = candidates[index] + current_sum
            if current_sum == target:
                self.res.append(subset + [candidates[index]])
                return

            elif current_sum > target:
                return

            # i can either pick current num or skip
            backtrack(index + 1, current_sum, subset + [candidates[index]] )
            dup = candidates[index]
            while candidates[index] == dup:
                index += 1
            backtrack(index, current_sum - dup, subset[:])
            
        backtrack(0, 0, [])
        return self.res

candidates = [10,1,2,7,6,1,5]; target = 8;
exp = [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
]

candidates = [2,5,2,1,2]; target = 5; exp = [
[1,2,2],
[5]
]

sol = Solution()
got = sol.combinationSum2(candidates, target)
assert got == exp, f"got {got}"
