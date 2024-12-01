from typing import (
    List,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0; h = len(nums) - 1
        while l <= h:

            mid = l + ((h - l) >> 1)
            print(l, mid, h)
            if nums[mid] == target:
                return mid
                   h = mid - 1
            elif 

        return -1
         

s = Solution()
print(s.search([5, 1, 3], 5))
