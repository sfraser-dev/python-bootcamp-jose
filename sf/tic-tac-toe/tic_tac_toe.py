''' a simple tic-tac-toe game in the command line 
    note: pylint gives this a 10/10 score! '''
import sys
from random import randint

def grid_print(grid):
    ''' simple grid print '''
    print(*grid[0:3])
    print(*grid[3:6])
    print(*grid[6:9])
    print("")

def grid_construct():
    ''' simple grid template '''
    return ['-','-','-','-','-','-','-','-','-']

def check_input_value_in_valid_range(val):
    ''' simple in-range check '''
    if val not in range(0,9):
        print("error: input val must be in range 1-9, try again")
        return False
    return True

def check_grid_location_unused(loc,grid):
    ''' simple check if grid location has been taken already '''
    if grid[loc] != '-':
        print("error, position already taken, try again")
        return False
    return True

def human_turn(grid):
    ''' get human input and update grid with their choice '''
    while True:
        # input location grid for human    python loation grid
        # 1 2 3                            0 1 2
        # 4 5 6                            3 4 5
        # 7 8 9                            6 7 8
        try:
            user_input_val = int(input("human, please input a location in range 1-9: "))
        except ValueError:
            print("input unrecognised, please try again!")
            continue
        user_input_val -= 1     # python location grid
        valid_range = check_input_value_in_valid_range(user_input_val)
        if valid_range is False:
            continue
        valid_location = check_grid_location_unused(user_input_val,grid)
        if valid_range is True and valid_location is True:
            grid[user_input_val] = 'X'
            return grid

def computer_turn(grid):
    ''' generate computer input and update grid with its choice '''
    while True:
        r_int = randint(1,9)    # return random int between 1 and 9 (including 1 and 9)
        print(f'computer selects position {r_int}')
        #input("hit enter to continue")
        r_int -= 1              # python location grid
        valid_range = check_input_value_in_valid_range(r_int)
        if valid_range is False:
            continue
        valid_location = check_grid_location_unused(r_int,grid)
        if valid_range is True and valid_location is True:
            grid[r_int] = 'O'
            return grid

def check_rows_cols_diags_if_all_x_or_all_o(str_arr):
    ''' check if a row, column or diagonal is full with Xs or Os '''
    if '-' in str_arr:
        return False
    # check all chars against the first char to see if all match
    return all(x==str_arr[0] for x in str_arr)

def check_rows_cols_diags_for_winner(grid):
    ''' check for 3 in a row in rows, columns and diagonals '''
    row1= grid[0:3]
    row2= grid[3:6]
    row3= grid[6:9]
    col1= [grid[0], grid[3], grid[6]]
    col2= [grid[1], grid[4], grid[7]]
    col3= [grid[2], grid[5], grid[8]]
    diag_nw_se = [grid[0], grid[4], grid[8]]
    diag_sw_ne = [grid[6], grid[4], grid[2]]
    if check_rows_cols_diags_if_all_x_or_all_o(row1) is True:
        print(f"winner is {row1[0]}, game over!\n")
        sys.exit()
    elif check_rows_cols_diags_if_all_x_or_all_o(row2) is True:
        print(f"winner is {row2[0]}, game over!\n")
        sys.exit()
    elif check_rows_cols_diags_if_all_x_or_all_o(row3) is True:
        print(f"winner is {row3[0]}, game over!\n")
        sys.exit()
    elif check_rows_cols_diags_if_all_x_or_all_o(col1) is True:
        print(f"winner is {col1[0]}, game over!\n")
        sys.exit()
    elif check_rows_cols_diags_if_all_x_or_all_o(col2) is True:
        print(f"winner is {col2[0]}, game over!\n")
        sys.exit()
    elif check_rows_cols_diags_if_all_x_or_all_o(col3) is True:
        print(f"winner is {col3[0]}, game over!\n")
        sys.exit()
    elif check_rows_cols_diags_if_all_x_or_all_o(diag_nw_se) is True:
        print(f"winner is {diag_nw_se[0]}, game over!\n")
        sys.exit()
    elif check_rows_cols_diags_if_all_x_or_all_o(diag_sw_ne) is True:
        print(f"winner is {diag_sw_ne[0]}, game over!\n")
        sys.exit()
    else:
        pass

def check_if_grid_full(grid):
    ''' is the grid full? '''
    if '-' not in grid:    # all cells taken
        print("it's a draw, game over!")
        sys.exit()

def play_game(grid):
    ''' game loop '''
    while True:
        grid = human_turn(grid)
        grid_print(grid)
        check_rows_cols_diags_for_winner(grid)
        check_if_grid_full(grid)
        #input("hit enter to continue")
        grid = computer_turn(grid)
        grid_print(grid)
        check_rows_cols_diags_for_winner(grid)
        check_if_grid_full(grid)

if __name__ == '__main__':
    the_grid = grid_construct()
    grid_print(the_grid)
    play_game(the_grid)
