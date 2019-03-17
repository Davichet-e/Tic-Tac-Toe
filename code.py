def tic_tac_toe():

    def win_condition(symbol):
        '''
        Checks if a player wins
        '''
        return ((board[15] == board[21] == board[27] == symbol)
            or (board[49] == board[55] == board[61] == symbol) 
            or (board[83] == board[89] == board[95] == symbol)
            or (board[15] == board[49] == board[83] == symbol)
            or (board[21] == board[55] == board[89] == symbol) 
            or (board[27] == board[61] == board[95] == symbol)
            or (board[15] == board[55] == board[95] == symbol)
            or (board[27] == board[55] == board[83] == symbol))
    print("Welcome to Tic-Tac-Toe!")
    boar = '     |     |\n     |     |   \n-----|-----|-----\n     |     |   \n-----|-----|-----\n     |     |   \n     |     |'
    board = [x for x in boar]
    sel_dict = {'a1':15, 'a2':21, 'a3':27, 'b1':49, 'b2':55, 'b3':61, 'c1':83, 'c2':89, 'c3':95}
    select_board = '     |     |\n a1  | a2  | a3 \n-----|-----|-----\n b1  | b2  | b3\n-----|-----|-----\n c1  | c2  | c3\n     |     |'
    print(select_board)
    i = 0

    while i < 9: 
        selection = input('Select box:')
 
        if i%2==0:
            try:
                if board[sel_dict[selection]] == " ": # Only if the box have not been selected before 
                    board[sel_dict[selection]] = 'x'
                    i += 1 
                else:
                    print("Box already selected!")

            except:
                print('Invalid box!')
            print_board = ''
            for x in board:
                print_board += x
            print(print_board)
            if win_condition('x'):
                print("Congratulations, player1 won!")
                rematch = input("Do you want to play again? (y/n)\n")
                if rematch == "y":
                    tic_tac_toe()
                break
        else:
            try:
                if board[sel_dict[selection]] == " ":
                    board[sel_dict[selection]] = "o" 
                    i += 1
                else:
                    print("Box already selected!")
            except:
                print('Invalid box!')
            print_board = ''
            for x in board:
                print_board += x
            print(print_board)
            if win_condition('o'):
                print("Congratlations, player2 won!")
                rematch = input("Do you want to play again? (y/n)\n")
                if rematch == "y":
                    tic_tac_toe()
                break
        if i == 9:
            print("It is a tie!")
            rematch = input("Do you want to play again? (y/n)\n")
            if rematch == "y":
                tic_tac_toe()
tic_tac_toe()
