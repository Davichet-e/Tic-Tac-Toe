i = 0


def tic_tac_toe():
    global i

    def win_condition(symbol):
        return ((board[15] == board[21] == board[27] == symbol)
                or (board[49] == board[55] == board[61] == symbol)
                or (board[83] == board[89] == board[95] == symbol)
                or (board[15] == board[49] == board[83] == symbol)
                or (board[21] == board[55] == board[89] == symbol)
                or (board[27] == board[61] == board[95] == symbol)
                or (board[15] == board[55] == board[95] == symbol)
                or (board[27] == board[55] == board[83] == symbol))

    def reset():
        global i
        rematch = input("Do you want to play again? (y/n)\n")
        if rematch == "y" or rematch == "yes":
            i = 0
            tic_tac_toe()
            return True
        else:
            print("Goodbye! Thanks for playing.")

    def turn(symbol):
        global i
        selection = input('Select box:')
        try:
            if board[sel_dict[selection]] == " ":
                board[sel_dict[selection]] = symbol
                i += 1
            else:
                print("Box already selected!")

        except KeyError:
            print('Invalid box!')
        print_board = ''
        for x in board:
            print_board += x
        print(print_board)

    print("Welcome to Tic-Tac-Toe!")
    boar = '     |     |\n     |     |   \n-----|-----|-----\n     |     |   \n-----|-----|-----\n     |     |   \n     |     |'
    board = [x for x in boar]
    sel_dict = {'a1': 15, 'a2': 21, 'a3': 27, 'b1': 49,
                'b2': 55, 'b3': 61, 'c1': 83, 'c2': 89, 'c3': 95}
    select_board = '     |     |\n a1  | a2  | a3 \n-----|-----|-----\n b1  | b2  | b3\n-----|-----|-----\n c1  | c2  | c3\n     |     |'
    print(select_board)

    while i < 9:
        if i % 2 == 0:
            turn("x")
            if win_condition("x"):
                print("Congratulations, Player1 won!")
                reset()
                break
        else:
            turn("o")
            if win_condition("o"):
                print("Congratulations, Player2 won!")
                reset()
                break
        if i == 9:
            print("It is a tie!")
            reset()
            break


tic_tac_toe()
