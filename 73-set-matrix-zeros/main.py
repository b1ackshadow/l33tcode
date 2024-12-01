from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix); c = len(matrix[0])
        def print_matrix():
            for i in range(r):
                for j in range(c):
                    print(matrix[i][j], end=" ")

                print()
            print()
        # r_mark = set()
        # c_mark = set()

        # print_matrix()
        col_0 = 1
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    print(f"zreo {i}, {j}")
                    if j == 0:
                        col_0 = 0
                    else:
                        matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        # print(f"{i},{j}")
                        # print(matrix[i][0], matrix[0][j])
                        # print()
                        matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(1, c):
                matrix[0][j] = 0

        if col_0 == 0:
            for i in range(r):
                matrix[i][0] = 0

        print_matrix()


s = Solution()
# (s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])

