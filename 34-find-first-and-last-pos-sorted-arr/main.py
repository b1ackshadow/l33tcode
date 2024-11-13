from typing import List
class Solution:
    def binSearch(self, lo, hi, nums, target):
        # print(f"Finding {target} in [{lo}, {hi}]")
        while lo <= hi:
            mid = (lo + hi ) // 2
            # print(f"mid = {nums[mid]}")
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0; hi = len(nums) - 1
        start = -1
        end = -1
        start = self.binSearch(lo, hi, nums, target)
        # print(f"Found {target} at {start}")
        if(start == -1):
            return [-1, -1]
        end = self.binSearch(start, hi, nums, target + 1) - 1
        print(f"start = {start} end = {end}")
        if start < len(nums) and nums[start] == target:
            return [start, end]
        return [-1, -1]

        # find start
        # while lo <= hi:
        #     mid = (lo + hi ) // 2
        #     if nums[mid] == target:
        #         if mid > 0 and nums[mid - 1] == target:
        #             hi = mid - 1
        #         else:
        #             start = mid
        #             break
        #     elif nums[mid] > target:
        #         hi = mid - 1
        #     else:
        #         lo = mid + 1
        # # print(f"found start {start}")
        # lo = 0; hi = len(nums) - 1
        # while lo <= hi:
        #     mid = (lo + hi ) // 2
        #     if nums[mid] == target:
        #         if mid < len(nums)-1 and nums[mid + 1] == target:
        #             lo = mid + 1
        #         else:
        #             end = mid
        #             break
        #     elif nums[mid] > target:
        #         hi = mid - 1
        #     else:
        #         lo = mid + 1
        # print(f"found end {end}")

        return [start, end]
        

sol = Solution()

tests = [
    ([5,7,7,8,8,10], 8, [3,4]),
    ([1], 1, [0,0]),
    ([3,3,3], 3, [0, 2]),
    ([5,7,7,8,8,10],8, [3, 4]),
    ([5,7,7,8,8,10],6, [-1, -1]),
    ([], 0, [-1, -1])
]

for i, (nums, target, expected) in enumerate(tests):
    try:
        got = sol.searchRange(nums, target )
        assert got == expected, f"Case {nums} -> {target} failed: expected {expected} but got {got}"
        print(f"Test case {i} passed")
    except Exception as e:
        print(str(e))
        pass
        # break

