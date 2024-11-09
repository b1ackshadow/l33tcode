from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0; high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            l_end = mid == 0; r_end = (mid == (len(nums) - 1)) 
            if (l_end or nums[mid] > nums[mid-1]) and (r_end or nums[mid] > nums[mid + 1]):
                # print(f"mid = {nums[mid]} l_end {l_end} r_end {r_end}")
                return mid
            elif mid != len(nums) - 1 and nums[mid] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1

sol = Solution()
test_cases = [
    # Format: (nums, expected_output)
    
    # Single element
    ([1], 0),

    # Two elements
    ([1, 2], 1),
    ([2, 1], 0),

    # Increasing sequence
    ([1, 2, 3, 4], 3),

    # Decreasing sequence
    ([4, 3, 2, 1], 0),

    # Peaks in the middle
    ([1, 3, 2, 1], 1),
    ([1, 2, 3, 2, 1], 2),
    ([1, 3, 2, 4, 3], [1, 3]),  # Multiple valid peaks
]

for i, (nums, expected) in enumerate(test_cases):
    # print(f"Checking test case {i}, inp = {nums}")
    result = sol.findPeakElement(nums)
    if isinstance(expected, list):
        assert result in expected, f"Test case {i} failed: got {result}, expected one of {expected}"
    else:
        assert result == expected, f"Test case {i} failed: got {result}, expected {expected}"
    print(f"Test case {i} passed with output {result}")
