from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low
        
sol = Solution()
nums = [1,3,5,6]; target = 5
print(sol.searchInsert(nums,target))
nums = [1,3,5,6]; target = 2
print(sol.searchInsert(nums,target))
nums = [1,3,5,6]; target = 7
print(sol.searchInsert(nums,target))
