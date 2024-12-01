from typing import List

class Solution:
    def valid_move(self, x,y):
        return (0 <= x < self.m) and (0 <= y < self.n) and self.grid[x][y] != "0"

    def move(self, x, y, direction):
        # x is row and y is column
        dir_map = {
            "RIGHT":0,
            "DOWN":1,
            "LEFT":2,
            "UP": 3
        }
        step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x_step, y_step = step[dir_map[direction]]
        new_pos = (x + x_step, y + y_step)
        return new_pos

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid); self.n = len(grid[0])

        islands = 0
        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c] == "1":
                    self.grid[r][c] = "0"
                    self.dfs(r,c)

                    islands += 1

        return islands

        

    def dfs(self, r, c):
        moves = [
            self.move(r,c, "UP"),
            self.move(r,c, "DOWN"),
            self.move(r,c, "RIGHT"),
            self.move(r,c, "LEFT")
        ]
        # print([ ((x,y), self.valid_move(x,y)) for (x,y) in moves])
        # return

        for move in moves:
            x, y = move
            if self.valid_move(x,y) and self.grid[x][y] == "1":
                self.grid[x][y] = "0"
                self.dfs(x,y)

        return


s = Solution()
# print(s.numIslands([
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]]))
print(s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
