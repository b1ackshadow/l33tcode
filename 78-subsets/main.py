from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.pick(nums, 0, [])
        return self.result
    def pick(self, nums, index, current):

        if index == len(nums):
            self.result.append(current)
            return current

        self.pick(nums, index + 1, current + [nums[index]])
        self.pick(nums, index + 1, current)

        

tests = [
    ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ([0], [[],[0]])
]

sol = Solution()

for i, (inp, want) in enumerate(tests):

    got = sol.subsets(inp)
    print(got)



