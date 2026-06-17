class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check columns
        for row in range (9):
            track = set()
            for col in range(9):
                # print(track)
                if board[row][col] in track:
                    return False
                elif board[row][col] != ".":
                    track.add(board[row][col])

        # check rows
        for col in range (9):
            track = set()
            for row in range(9):
                # print(track)
                if board[row][col] in track:
                    return False
                elif board[row][col] != ".":
                    track.add(board[row][col])

        # check 3x3 boxes
        for row_offset in range (3):
            # print(f"row_offset: ", row_offset)
            for col_offset in range (3):
                # print(f"col_offset: ", col_offset)
                track = set()
                for row in range (row_offset*3, row_offset*3+3):
                    for col in range (col_offset*3, col_offset*3+3):
                        # print(f"current board: ", board[row][col])
                        # print(track)
                        if board[row][col] in track:
                            return False
                        elif board[row][col] != ".":
                            track.add(board[row][col])
        return True
