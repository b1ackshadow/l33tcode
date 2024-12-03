from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        r = 0; b = len(nums) - 1

        for i, color in enumerate(nums):
            if color == 0:
                nums[r], nums[i] = nums[i], nums[r]
                r += 1
            elif color == 2:
                nums[b], nums[i] = nums[i], nums[b]
                b -= 1


        print(nums)
        

s = Solution()

(s.sortColors([2,0,2,1,1,0]))
