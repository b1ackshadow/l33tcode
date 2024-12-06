from typing import List

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#
#         r = len(board); c = len(board[0])
#         self.r = r; self.c = c
#         self.board = board
#         self.visited = set()
#         self.reachable = set()
#
#         for i in range(r):
#             for j in range(c):
#
#                 if board[i][j] == 'O':
#                 # we need to find if this can reach boundary or not
#                     reachable = self.explore(i, j)
#                     if not reachable:
#                         board[i][j] = "X"
#                     else:
#                         self.reachable.add((i, j))
#
#     def explore(self, x, y):
#         print(f"exploring {x},{y}")
#         # self.visited.add((x, y))
#
#         def valid(x, y):
#             return not (
#                 x < 0 or x == self.r or
#                 y < 0 or y == self.c or
#                 self.board[x][y] != "O"
#             )
#
#         # if the cell is on boundary its reachable so 
#         if x == 0 or y == 0 or (x == self.r - 1) or (y == self.c - 1):
#             print(f"boundary cell {x}, {y}")
#             return True
#
#         # if not we try to see if it can reach boundary through neighbors indirectly
#
#
#         directions = [(1, 0), (-1, 0), (0, 1),(0, -1)]
#
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if valid(nx, ny):
#                 reachable = True
#                 if (nx, ny) not in self.reachable:
#                     reachable = self.explore(nx, ny)
#                 if reachable:
#                     self.board[x][y] = "O"
#                     return True
#
#         self.board[x][y] = "X"
#         return False

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.board = board
        self.r = len(board); self.c = len(board[0])
        r = self.r; c = self.c

        self.reachable = set()
        queue = []

        for x in range(r):
            if board[x][0] == 'O':
                queue.append((x, 0))
            if board[x][c - 1] == "O":
                queue.append((x, c - 1))

        for y in range(c):
            if board[0][y] == 'O':
                queue.append((0, y))
            if board[r - 1][y] == "O":
                queue.append((r - 1, y))


        directions = [(1, 0), (-1, 0), (0, 1),(0, -1)]
        while queue:
            x, y = queue.pop(0)
            self.reachable.add((x, y))


            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if self.valid(nx, ny):
                    if (nx, ny) not in self.reachable:
                        queue.append((nx, ny))


        for x in range(r):
            for y in range(c):
                if board[x][y] == "O" and (x, y) not in self.reachable:
                    board[x][y] = "X"


    def valid(self, x, y):
        return not (
            x < 0 or x == self.r or
            y < 0 or y == self.c or
            self.board[x][y] != "O"
        )

s = Solution()

board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
board = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]

board = [["O","X","O","O","O","X"],
         ["O","O","X","X","X","O"],
         ["X","X","X","X","X","O"],
         ["O","O","O","O","X","X"],
         ["X","X","O","O","X","O"],
         ["O","O","X","X","X","X"]]

s.solve(board)

assert board == [["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]], "Failed"
print(board)
