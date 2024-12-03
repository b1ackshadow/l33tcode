from typing import List


class Solution:
    def get_moves(self, x, y):
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        return [ (x + x_d, y + y_d ) for (x_d, y_d) in directions]

    def is_valid(self, x, y):
        if x < 0 or x == self.r or y < 0 or y == self.c or self.grid[x][y] != 1:
            return False
        return True

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        print(grid)

        self.r = len(grid); self.c = len(grid[0])

        queue = []
        fresh_oranges = 0
        for i in range(self.r):
            for j in range(self.c):
                if self.grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif self.grid[i][j] == 1:
                    fresh_oranges += 1

        total_time = 0
        while queue:
            (x, y, time) = queue.pop(0)
            # print(f"Processing cell {x},{y} at {time}")

            # mark this as rotten
            # add possible neighbors for this cell to queue with time + 1
            moves = self.get_moves(x,y)
            for move in moves:
                if self.is_valid(*move):
                    x, y = move
                    if self.grid[x][y] == 1:
                        fresh_oranges -= 1
                    self.grid[x][y] = 2
                    # print(f"found neighbor {x},{y}")
                    queue.append((x, y, time + 1))


            total_time = time
        return total_time if fresh_oranges == 0 else -1


        

s = Solution()

grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]

print(s.orangesRotting(grid))
print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(s.orangesRotting([[0,2]]))
print(s.orangesRotting([[2,2],[1,1],[0,0],[2,0]]))
# t = [[2,2],
#      [1,1],
#      [0,0],
#      [2,0]]
#

