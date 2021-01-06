def board_state(sudoku):
    bin_board =[];
    for row in sudoku:
        bool_row = [];
        for element in row:
            if(element != 0):
                bool_row.append(True)
            else:
                bool_row.append(False)
        bin_board.append(bool_row)
    return bin_board

def update_column_no(col_no):
    if col_no  <8:
        col_no+=1
    else:
        col_no =0
    return col_no

def update_row_no(row_no, column_no):
    if column_no == 0:
        return row_no + 1
    return row_no

def solve(sudoku, bin_board, row_no = 0, col_no = 0):
    board(sudoku)
    if not bin_board[row_no][col_no]:
        for num in range(1, len(sudoku)+1):
            if fits(sudoku,num, row_no, col_no):
                sudoku[row_no][col_no] = num

                new_col_no = update_column_no(col_no)
                new_row_no = update_row_no(row_no, new_col_no)

                if new_row_no == 9:
                    return True
                if solve(sudoku, bin_board, new_row_no, new_col_no):
                    return True
        sudoku[row_no][col_no] = 0
        return False;
    else:
        new_col_no = update_column_no(col_no)
        new_row_no = update_row_no(row_no, new_col_no)

        if new_row_no == 9:
            return True
        if solve(sudoku, bin_board, new_row_no, new_col_no):
            return True

def fits(sudoku, num, row_no, col_no):
    if num in sudoku[row_no]:
        return False
    for i in range(9):
        if num == sudoku[i][col_no]:
            return False
    square = get_square(sudoku, row_no, col_no)
    if num in square:
        return False
    return True

def get_square(sudoku, row_no, col_no):
    row_no = row_no //3
    col_no = col_no //3
    square = sudoku[row_no*3: row_no*3+3]
    returnable =  []
    for i in range(len(square)):
        returnable += square[i][col_no*3: col_no*3 +3]
    return returnable




def sudoku_solver(sudoku):
    bin_board = board_state(sudoku)
    solve(sudoku, bin_board)
    return sudoku


def board(sudoku):
    print("*"*30)
    row_no = 0
    for row in sudoku:
        col_no = 0
        if not row_no %3 and row_no:
            print("-"*30)
        for elem in row:
            if not col_no %3 and col_no:
                print(" || ",end="")
            print(elem, end=" ")
            col_no +=1
        print("")
        row_no += 1
    print("*" * 30)
    print("")

import sys

if __name__ == "__main__":
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().split())))
    board(sudoku)
    sudoku_solver(sudoku)
    board(sudoku)