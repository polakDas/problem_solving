# Leetcode problem no 36. Valid Sudoku

import collections


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    continue
                if (board[row][column] in rows[row] or
                    board[row][column] in columns[column] or
                    board[row][column] in boxes[(row//3, column//3)]):
                    return False
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                boxes[((row//3, column//3))].add(board[row][column])
        print(f'Rows = {rows.values()}')
        print(f'Columns = {columns.values()}')
        print(f'Boxes = {boxes.values()}')

        return True

if __name__ == '__main__':
    board1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    board2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    board3 = [[".",".",".",".","5",".",".","1","."]
            ,[".","4",".","3",".",".",".",".","."]
            ,[".",".",".",".",".","3",".",".","1"]
            ,["8",".",".",".",".",".",".","2","."]
            ,[".",".","2",".","7",".",".",".","."]
            ,[".","1","5",".",".",".",".",".","."]
            ,[".",".",".",".",".","2",".",".","."]
            ,[".","2",".","9",".",".",".",".","."]
            ,[".",".","4",".",".",".",".",".","."]]

    solve = Solution()
    print(solve.isValidSudoku(board=board1))