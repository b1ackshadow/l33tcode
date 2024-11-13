from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0; hi = len(nums) -1
        while lo < hi:
            mid = lo + ((hi - lo) >> 2)
            # print(lo, hi)
            if nums[mid] > nums[-1]:
                lo = mid + 1
            else:
                hi = mid 

        return nums[lo]
        
        


tests = [
    ([3,4,5,1,2], 1),
    ([4,5,6,7,0,1,2], 0),
    ([11,13,15,17], 11)
]

sol = Solution()
for i, (nums, expected) in enumerate(tests):
    try:
        got = sol.findMin(nums)
        assert got == expected, f"Case {nums}: expected {expected} but got {got}"
        print(f"Test case {i} passed")
    except Exception as e:
        print(str(e))
        break
