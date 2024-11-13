from typing import List
class Solution:
    def __init__(self):
        self.bit_freq = [0] * 32 # cuz int32

    def get_or(self):
        num = 0
        for i, each in enumerate(self.bit_freq):
            bit = int(each > 0)
            num = num | (bit << i)
        return num

    # def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
    #     start = 0
    #     end = 0
    #     min_len = float("inf")
    #     window = 0
    #
    #     while end < len(nums):
    #         # Expand the window by including nums[end]
    #         window = window | nums[end]
    #         print(f"Adding nums[{end}] = {nums[end]} ({bin(nums[end])}), updated window OR = {window} (binary: {bin(window)})")
    #         self.set_bit(nums[end])
    #
    #         # Check if the current window meets the requirement
    #         if window >= k:
    #             print(f"Window meets or exceeds k = {k} with window OR = {window}")
    #
    #             # Try to shrink the window from the left (start pointer)
    #             while start <= end and window >= k:
    #                 min_len = min(min_len, end - start + 1)
    #                 print(f"Current min_len = {min_len}, checking to reduce window size")
    #                 print(f"Window OR before reducing: {window} (binary: {bin(window)})")
    #                 print(f"Removing nums[{start}] = {nums[start]} from window")
    #
    #                 # Reset bits for nums[start] and move start pointer to the right
    #                 self.reset_bit(nums[start])
    #                 start += 1
    #
    #                 # Update the window OR after removing nums[start-1]
    #                 window = self.get_or()
    #                 print(f"Updated window OR after removal = {window} (binary: {bin(window)})")
    #
    #         # Move end pointer to the right to expand the window
    #         end += 1
    #
    #     # Check if a valid subarray was found
    #     if min_len == float('inf'):
    #         print("No valid subarray found that meets or exceeds k.")
    #         return -1
    #
    #     print(f"Shortest subarray length with OR >= k: {min_len}")
    #     return int(min_len)

    def minimumSubarrayLength1(self, nums: List[int], k: int) -> int:
        start = 0; end = 0;

        min_len = float("inf")
        window = 0
        while end < len(nums):
            window = window | nums[end]
            print(f"num {nums[end]} -> window {window}")
            self.set_bit(nums[end])
            if window >= k:
                # print(f"bit freq {self.bit_freq}")

                # see if we can reduce
                while start <= end and window >= k:
                    min_len = min(min_len, end - start + 1)
                    print(f"min_len = {min_len}")
                    print(f"window bit {self.get_or()}")
                    print(f" resetting {bin(nums[start])}")
                    self.reset_bit(nums[start])
                    start += 1
                    window = self.get_or()
                    print(f"updated window {window}")
            end += 1

        if min_len == float('inf'):
            return -1
        return int(min_len)
                    


    def set_bit(self, num):
        index = 0
        while num > 0:
            bit = num & 1
            self.bit_freq[index] += bit
            num >>= 1
            index += 1

    def reset_bit(self, num):
        index = 0
        print(self.bit_freq)
        print(f"BEFORE {self.get_or()}")
        while num > 0:
            bit = num & 1
            if bit == 1:
                if self.bit_freq[index] > 0:
                    print(f"current bit at {i} = {self.bit_freq[i]}")
                    self.bit_freq[index] -= bit
            num >>= 1
            index += 1
        print(self.bit_freq)
        print(f"AFTER {self.get_or()}")




tests = [
    # ([1,2,3], 2, 1),
    # ([2,1,8], 10, 3),
    # ([1,2], 0, 1),
    # ([1, 2, 5, 8, 3, 1], 8, 1),
    # ([1,2,7,8,1], 8, 1),
    ([1,2,12,50,96,1], 93, 1)
]

sol = Solution()

for i, (nums, k, wanted) in enumerate(tests):
    try:
        got = sol.minimumSubarrayLength(nums, k)
        assert wanted == got, f"{nums} -> {k} :  Wanted {wanted} but got {got}"
        print(f"Test case {i + 1} passed")
    except Exception as e:
        print(str(e))
        break
