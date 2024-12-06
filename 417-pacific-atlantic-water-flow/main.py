from typing import List

class Solution:

    def get_moves(self, x, y):

        directions = [
            (-1, 0), # U
            (0, -1), # L
            (0, 1),  # R
            (1, 0), # D
        ]
        return [ (x + x_d, y + y_d) for (x_d, y_d) in directions]
    
    def pacificAtlantic_dfs(self, heights: List[List[int]]) -> List[List[int]]:
        self.pacific = set()
        self.atlantic = set()
        self.visited = set()
        self.heights = heights
        self.r = len(heights); self.c = len(heights[0])

        # mark coasts as reachable 

        for i in range(self.r):
            self.pacific.add((i, 0))
            self.visited.add((i, 0))
        for i in range(self.c):
            self.pacific.add((0, i))
            self.visited.add((0, i))

        for i in range(self.r):
            self.atlantic.add((i, self.c - 1))
            self.visited.add((i, self.c - 1))
        for i in range(self.c):
            self.atlantic.add((self.r - 1, i))
            self.visited.add((self.r - 1, i))

        for i in range(self.r):
            for j in range(self.c):
                # whether this is already flooded then we can search 
                if (i, j) in self.pacific:
                    self.dfs(i, j, self.pacific)
                if (i, j) in self.atlantic:
                    self.dfs(i, j, self.atlantic)

        return self.pacific & self.atlantic


    def dfs(self, x, y, ocean):

        moves = self.get_moves(x, y)

        for move in moves:
            x_n, y_n = move
            if (
                self.is_valid(x_n, y_n) 
                and self.heights[x][y] <= self.heights[x_n][y_n]
                and (move not in ocean)
            ):
                ocean.add(move)
                self.dfs(*move, ocean)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        p_queue = []
        a_queue = []
        r = len(heights); c = len(heights[0])

        for i in range(r):
            p_queue.append((i, 0))
            a_queue.append((i, c - 1))

        for i in range(c):
            p_queue.append((0, i))
            a_queue.append((r - 1, i))

        def bfs(queue, r, c):
            def is_valid(x, y):
                if x < 0 or x == r or y < 0 or y == c:
                    return False
                return True
            reachable = set()
            directions = [
                (-1, 0), # U
                (0, -1), # L
                (0, 1),  # R
                (1, 0), # D
            ]

            while queue:
                x, y = queue.pop(0)
                reachable.add((x, y))

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if is_valid(nx, ny) and (nx, ny) not in reachable and heights[x][y] <= heights[nx][ny]:
                        queue.append((nx, ny))


            return reachable


        p_reachable = bfs(p_queue, r, c)
        a_reachable = bfs(a_queue, r, c)

        return list(p_reachable & a_reachable)


    def is_valid(self, x, y):
        if x < 0 or x == self.r or y < 0 or y == self.c:
            return False
        return True



s = Solution()

grid = [[1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]]

print(s.pacificAtlantic(grid))
