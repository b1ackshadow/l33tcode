# Flipping a subset of columns is like doing a bitwise XOR of some number K onto each row.
# We want rows X with X ^ K = all 0s or all 1s.
# This is the same as X = X^K ^K = (all 0s or all 1s) ^ K, so we want to count rows that have opposite bits set.
# For example, if K = 1, then we count rows X = (00000...001, or 1111....110).

from typing import List

class Solution:

    def flip(self, row: List[int]) -> List[int]:
        return [int(not v) for v in row]
    
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        same_pattern = {}

        for row in matrix:
            pattern = tuple(row)
            flip_pattern = tuple(self.flip(row))

            same_pattern[pattern] = same_pattern.get(pattern, 0) + 1
            same_pattern[flip_pattern] = same_pattern.get(flip_pattern, 0) + 1

        # print(same_pattern)
        return max(same_pattern.values())





s = Solution()

# print(s.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))
print(s.maxEqualRowsAfterFlips([[0,1],[1,1]]))
