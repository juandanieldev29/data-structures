from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False

                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

        return True


    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     obj_board = {}
    #     length_rows = len(board) - 1
    #     for index_x, x in enumerate(board):
    #         seen_row = {}
    #         for index_y, _ in enumerate(x):
    #             cell_value = board[index_x][index_y]
    #             coordinates = (index_x, index_y)
    #             if cell_value != ".":
    #                 seen_row[coordinates] = cell_value
    #                 obj_board[coordinates] = cell_value
    #             if index_x == length_rows:
    #                 column_result = self.check_columns(obj_board, length_rows, index_y)
    #                 if not column_result:
    #                     return False
    #             if (index_x + 1) % 3 == 0 and (index_y + 1) % 3 == 0:
    #                 cross_result = self.check_sub_box(obj_board, index_x, index_y)
    #                 if not cross_result:
    #                     return False
    #         row_result = self.check_rows(seen_row)
    #         if not row_result:
    #             return False
    #     return True


    # def check_rows(self, seen_row: dict[tuple[int, int], str]) -> bool:
    #     seen_row_vals = set()
    #     for _, item in seen_row.items():
    #         if item in seen_row_vals:
    #             return False
    #         seen_row_vals.add(item)
    #     return True

    # def check_sub_box(self, obj_board: dict[tuple[int, int], str], row: int, column: int) -> bool:
    #     seen_vals = set()
    #     for _ in range(3):
    #         current_row = row
    #         for _ in range(3):
    #             item = obj_board.get((current_row, column), None)
    #             if item in seen_vals:
    #                 return False
    #             if item is not None:
    #                 seen_vals.add(item)
    #             current_row -= 1
    #         column -= 1
    #     return True
    

    # def check_columns(self, obj_board: dict[tuple[int, int], str], length_rows: int, row: int) -> bool:
    #     seen_col_vals = set()
    #     for x in range(length_rows, -1, -1):
    #         item = obj_board.get((x, row), None)
    #         if item in seen_col_vals:
    #             return False
    #         if item is not None:
    #             seen_col_vals.add(item)
    #     return True
    
# board = [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# board = [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
        #  [".",".",".",".",".","3",".",".","1"],
         [".",".",".",".",".","4",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]

solution = Solution()
result = solution.isValidSudoku(board)
print(result)
