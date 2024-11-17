from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # visited = [
        #     [False for _ in range(len(board[0]))] for _ in range(len(board)) 
        # ]
        #
        def search(x, y, w_index) -> bool:
            if (
                x < 0 
                or x == len(board) 
                or y < 0 
                or y == len(board[0]) 
                or w_index == len(word)
                or board[x][y] != word[w_index]
                # or visited[x][y]
            ):
                return False
            # visited[x][y] = True
            board[x][y] = '@'

            if w_index + 1 == len(word):
                return True
            # UP
            res = search(x - 1, y, w_index + 1) #, visited[:])
            if res:
                return res
            # DOWN
            res = search(x + 1, y, w_index + 1) # , visited[:])
            if res:
                return res

            # LEFT
            res = search(x , y - 1, w_index + 1) #, visited[:])
            if res:
                return res
            # RIGHT
            res = search(x, y + 1, w_index + 1) #, visited[:])
            # visited[x][y] = False
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    res = search(r, c, 0)
                    if res:
                        return res
        
        return False


tests = [
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False)
]

sol = Solution()
for i, (board, word, want) in enumerate(tests):
    got = sol.exist(board, word)
    assert got == want, f"Case {i} got {got}"
