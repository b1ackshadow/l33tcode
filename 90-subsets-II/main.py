from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = [[]]
        self.pick(sorted(nums), 0, [])
        return self.result

    def pick(self, nums, index, current):

        if index == len(nums) :
            if current:
                self.result.append(current)
            return 

        self.pick(nums, index + 1, current + [nums[index]])
        dup = nums[index]
        while index < len(nums) and nums[index] == dup:
            index += 1
        self.pick(nums, index, current)



tests = [
    # ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ([1,2,2],[[],[1],[1,2],[1,2,2],[2],[2,2]]),
    ([0], [[],[0]])
]

sol = Solution()

for i, (inp, want) in enumerate(tests):

    got = sol.subsets(inp)
    print(got)
