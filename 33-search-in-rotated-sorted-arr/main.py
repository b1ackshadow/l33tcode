
class Solution:
    def search(self, nums, target):
        # Your implementation of the search function
        low = 0; high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if not (nums[mid] < nums[0]) ==  (target < nums[0]):
                if target < nums[0]:
                    nums[mid] = float("-inf")
                else:
                    nums[mid] = float("inf")
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            print(nums)
                

        return -1

# Instantiate Solution
solution = Solution()

test_cases = [
    # Format: (nums, target, expected_output)
    ([4,5,6,7,8,1,2,3], 8, 4),
    # ([12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 14, 2),
    # ([12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 7, 15),
    # ([5,1,3], 5, 0),
    # ([1,3,5], 5, 2),
    # ([1], 0, -1),  # Single element array, target not found
    # ([4, 5, 6, 7, 0, 1, 2], 0, 4),  # Target found at index 4
    # ([4, 5, 6, 7, 0, 1, 2], 3, -1),  # Target not found, return -1
]

# Run tests
for i, (nums, target, expected) in enumerate(test_cases):
    result = solution.search(nums, target)
    assert result == expected, f"Test case {i} failed: got {result}, expected {expected}"
    print(f"Test case {i} passed with output {result}")


# [1,3,5] mid < target but low < target
# [5,1,3] mid < target but low >= target
# [3,5,1]
