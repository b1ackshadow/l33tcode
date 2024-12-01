from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def print_board(board):
            for i, val in enumerate(board):
                if i == 3:
                    print("\n")
                print(val, end=" ")

            print()
        possible_moves = [
            [1, 3],         # Possible moves for index 0
            [0, 2, 4],      # Possible moves for index 1
            [1, 5],         # Possible moves for index 2
            [0, 4],         # Possible moves for index 3
            [1, 3, 5],      # Possible moves for index 4
            [2, 4],         # Possible moves for index 5
        ]

        def get_new_state(a, b, state):
            """ Swap two positions in the state and return the new state as a string """
            state = list(state)
            state[a], state[b] = state[b], state[a]
            return "".join(state)

        # Flatten the input board and convert it into a string representation
        flat = [str(val) for row in board for val in row]
        board_state = "".join(flat)
        visited = {}

        print(f"Initial board state: {board_state}")


        def dfs(state, move):
            if state == "123450":
                return move
            empty_index = int(state.index("0"))

            moves = possible_moves[empty_index]

            for move in moves:
                new_state = get_new_state(empty_index, move, state)
                if new_state not in visited:
                    print("old")
                    print_board(state)
                    print("new")
                    print_board(new_state)
                    visited[new_state] = True
                    return dfs(new_state, move + 1)

            return -1



        return dfs(board_state, 0)

# Example usage:
s = Solution()
print(s.slidingPuzzle([[4, 1, 2], [5, 0, 3]]))

