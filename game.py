row0 = [' ' * 3]
row1 = [' ' * 3]
row2 = [' ' * 3]
winner_X_list = ['X' * 3]
winner_O_list = ['O' * 3]
is_X = True
is_winner = False


def gameloop(over_write=False):
    while True:
        print_board(row0, row1, row2)
        global is_X
        if over_right:
            print("You can't just overwrite something")
        row = clean_user_input()
        col = clean_user_input()
        mod_board(row, col, is_X)
        is_winner = check_for_winner(col)
        if is_winner:
            print('We have a winner')
            break
        if is_X == True:
            is_X = False
        else:
            is_X = True
        print("\n")


def clean_user_input():
    ''' This set col input for user and turns to a accpetable int'''
    choice_col = ' '
    accepted_col_range = range(0, 3)
    inside_col_range = False
    while(choice_col.isdigit() == False or inside_col_range == False):
        choice_col = input("Chose a number between 0 - 2: ")
        if choice_col.isdigit():
            if int(choice_col) in accepted_col_range:
                inside_col_range = True
    return(int(choice_col))


def print_board(row0, row1, row2):
    ''' Print the board'''
    print(row0)
    print(row1)
    print(row2)


def mod_board(row, col, is_x):
    '''apply changes when need to the board '''
    global row0
    global row1
    global row2

    if row == 0 and over_write_checker(row0[col]):
        if is_x == True:
            row0[col] = 'X'
        else:
            row0[col] = 'O'
    if row == 1 and over_write_checker(row1[col]):
        if is_x == True:
            row1[col] = 'X'
        else:
            row1[col] = 'O'
    if row == 2:
        if is_x == True and over_write_checker(row2[col]):
            row2[col] = 'X'
        else:
            row2[col] = 'O'

    def over_write_checker(row, col):
        if row[col] == ' ':
            return True
        else:
            gameloop(True)


def check_for_winner(col):
    global winner_X_list
    global winner_O_list
    global row0
    global row1
    global row2
    if row0[col] == row1[col] and row1[col] == row2[col]:
        return True
    elif row0[0] == row1[1] and row1[1] == row2[2]:
        return True
    elif row2[0] == row1[1] and row1[2] == row0[0]:
        return True
    elif row0 == winner_O_list or row0 == winner_X_list:
        return True
    elif row1 == winner_O_list or row1 == winner_X_list:
        return True
    elif row2 == winner_O_list or row2 == winner_X_list:
        return True
    else:
        False


gameloop()
