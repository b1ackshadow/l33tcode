from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        breakpoint = -1
        n = len(nums) - 1
        for i in range(n - 1, -1, -1):
            if nums[i] < nums[i + 1]:
                breakpoint = i
                break

        if breakpoint == -1:
            nums.reverse()
            print(nums)
            return 
        print(f"breakpoint {breakpoint}")
        # find the smallest number that is greather nums[breakpoint]
        next_number_idx = None
        for i in range(len(nums) - 1, breakpoint, -1):
            print(i)
            if nums[i] > nums[breakpoint]:
                next_number_idx = i
                break
                print(f"updated next number {next_number_idx}")

        nums[breakpoint], nums[next_number_idx] = nums[next_number_idx], nums[breakpoint]

        nums[breakpoint + 1: ] = (nums[-1:breakpoint:-1])


        print(nums)



        
s = Solution()
# s.nextPermutation([1,2,3])
# s.nextPermutation([3,2,1])
# s.nextPermutation([1,1,5])
s.nextPermutation([2,3,1,3,3])
