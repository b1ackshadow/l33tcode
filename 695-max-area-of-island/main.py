from typing import List
class Solution:

    def __init_grid(self, grid):
        self.grid = grid
        self.r = len(grid); self.c = len(grid[0])


    def print_grid(self):
        for i in range(self.r):
            for j in range(self.c):
                print(self.grid[i][j], end=" ")

            print()

        print()


    def get_moves(self, x,y):

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        moves = []
        for d in directions:
            x_delta, y_delta = d
            new_move = (x + x_delta,y + y_delta)
            # if valid_moves(new_move):
            moves.append(new_move)
        return moves

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.__init_grid(grid)

        for i in range(self.r):
            for j in range(self.c):

                if self.grid[i][j] != 0:
                    # start of an island
                    # grid[i][j] = 0
                    # print(f"Starting island at {i},{j}")
                    area = self.dfs(i, j)
                    max_area = max(max_area, area)

        return max_area


    def dfs(self, x, y) -> int:

        def is_valid(move):
            x, y = move
            if (x < 0) or (x == self.r) or (y < 0) or (y == self.c) or self.grid[x][y] == 0:
                return False
            return True

        # mark current island as visited
        self.grid[x][y] = 0
        moves = self.get_moves(x,y)
        
        local_area = 0
        for move in moves:
            if is_valid(move):
                x, y = move
                local_area += self.dfs(x,y)

        # print(f"local area for {x},{y} = {local_area}")
        return 1 + local_area


        

s = Solution()

test1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]


test1 = [[1,1,0,0,0],
         [1,1,0,0,0],
         [0,0,0,1,1],
         [0,0,0,1,1]]
print(s.maxAreaOfIsland(test1))
