from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float()

        current_sum = 0
        for num in nums:

            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

s = Solution()

print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([5,4,-1,7,8]))
print(s.maxSubArray([1]))
        
