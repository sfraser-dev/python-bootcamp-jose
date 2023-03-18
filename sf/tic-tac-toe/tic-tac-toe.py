import sys
from random import randint

def grid_print(g):
    print(*g[0:3])
    print(*g[3:6])
    print(*g[6:9])
    print("")

def grid_construct():
    g = ['-','-','-','-','-','-','-','-','-']
    return g

def check_input_value_in_valid_range(x):
    if x not in range(0,9):
        print("error: input val must be in range 1-9, try again")
        return False
    return True

def check_grid_location_unused(x,g):
    if g[x] != '-':
        print("error, position already taken, try again")
        return False
    return True

def human_turn(g):
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
        if valid_range == False:
            continue
        valid_location = check_grid_location_unused(user_input_val,g)
        if valid_range==True and valid_location==True:
           g[user_input_val] = 'X'
           return g
        
def computer_turn(g):
    while True: 
        r = randint(1,9)    # return random int between 1 and 9 (including 1 and 9)
        print(f'computer selects position {r}')
        #input("hit enter to continue")
        r -= 1                  # python location grid
        valid_range = check_input_value_in_valid_range(r)
        if valid_range == False:
            continue
        valid_location = check_grid_location_unused(r,g)
        if valid_range==True and valid_location==True:
            g[r] = 'O'
            return g
        
def check_if_all_Xs_or_all_Os(str_arr):
    if '-' in str_arr:
        return False
    # check all chars against the first char to see if all match
    return all(x==str_arr[0] for x in str_arr)

def check_rows_cols_diags_for_winner(g):
    row1= g[0:3]
    row2= g[3:6]
    row3= g[6:9]
    col1= [g[0], g[3], g[6]]
    col2= [g[1], g[4], g[7]]
    col3= [g[2], g[5], g[8]]
    diag_nw_se = [g[0], g[4], g[8]]
    diag_sw_ne = [g[6], g[4], g[2]]
    if check_if_all_Xs_or_all_Os(row1)==True:
        print(f"winner is {row1[0]}, game over!\n")    
        sys.exit()
    elif check_if_all_Xs_or_all_Os(row2)==True:
        print(f"winner is {row2[0]}, game over!\n")    
        sys.exit()
    elif check_if_all_Xs_or_all_Os(row3)==True:
        print(f"winner is {row3[0]}, game over!\n")    
        sys.exit()
    elif check_if_all_Xs_or_all_Os(col1)==True:
        print(f"winner is {col1[0]}, game over!\n")    
        sys.exit()
    elif check_if_all_Xs_or_all_Os(col2)==True:
        print(f"winner is {col2[0]}, game over!\n")    
        sys.exit()
    elif check_if_all_Xs_or_all_Os(col3)==True:
        print(f"winner is {col3[0]}, game over!\n")    
        sys.exit()
    elif check_if_all_Xs_or_all_Os(diag_nw_se)==True:
        print(f"winner is {diag_nw_se[0]}, game over!\n")    
        sys.exit()
    elif check_if_all_Xs_or_all_Os(diag_sw_ne)==True:
        print(f"winner is {diag_sw_ne[0]}, game over!\n")    
        sys.exit()
    else:
        pass

def check_if_grid_full(g):
    if '-' not in g:    # all cells taken
        print("it's a draw, game over!")
        sys.exit()

def play_game(g):
    while True:
        g = human_turn(g) 
        grid_print(g)
        check_rows_cols_diags_for_winner(g)
        check_if_grid_full(g)
        #input("hit enter to continue")
        g = computer_turn(g)
        grid_print(g)
        check_rows_cols_diags_for_winner(g)
        check_if_grid_full(g)

g = grid_construct()
grid_print(g)
play_game(g)