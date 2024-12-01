from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        lowest_neg = float('inf')
        neg_parity = 0
        rows = range(len(matrix)); cols = range(len(matrix[0]))
        
        for r in rows:
            for c in cols:
                e = matrix[r][c]
                if e < 0:
                    neg_parity += 1
                    if abs(e) < lowest_neg:
                        lowest_neg = -abs(e)
                total += abs(e)

        print(neg_parity, lowest_neg)


        if neg_parity % 2 == 0:
            return total
        return total + lowest_neg








matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
s = Solution()
##print(s.maxMatrixSum([[-10000,-10000,-10000],[-10000,-10000,-10000],[-10000,-10000,-10000]]))
print(s.maxMatrixSum([[10,-6,-6,-8],[-3,-7,-8,-9],[-4,-8,-5,-8],[-9,-9,-6,-8]]))
