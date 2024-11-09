from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        search_row = None
        for row in range(len(matrix)):
            if matrix[row][0] <= target <=matrix[row][-1]:
                search_row = row
                break
        if search_row is None:
            return False
        low = 0; high = len(matrix[0]) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[search_row][mid] == target:
                return True
            elif matrix[search_row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


sol = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 3
print(sol.searchMatrix(matrix, target))
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target = 13
print(sol.searchMatrix(matrix, target))
