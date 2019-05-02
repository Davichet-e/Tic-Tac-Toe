"""
    TODO
"""


def tic_tac_toe() -> None:
    counter: int = 0

    def win_condition(symbol) -> bool:
        return (
            board[15] == board[21] == board[27] == symbol
            or board[49] == board[55] == board[61] == symbol
            or board[83] == board[89] == board[95] == symbol
            or board[15] == board[49] == board[83] == symbol
            or board[21] == board[55] == board[89] == symbol
            or board[27] == board[61] == board[95] == symbol
            or board[15] == board[55] == board[95] == symbol
            or board[27] == board[55] == board[83] == symbol
        )

    def reset() -> bool:
        nonlocal counter
        rematch: str = input("Do you want to play again? (y/n)\n")
        if rematch in ("y", "yes"):
            counter = 0
            tic_tac_toe()
            return True
        else:
            print("Goodbye! Thanks for playing.")
            return False

    def turn(symbol: str) -> None:
        nonlocal counter
        selection: str = input("Select box:").strip().lower()
        try:
            if board[sel_dict[selection]] == " ":
                board[sel_dict[selection]] = symbol
                counter += 1
            else:
                print("Box already selected!")

        except KeyError:
            print("Invalid box!")
        print_board: str = ""
        for x in board:
            print_board += x
        print(print_board)

    print("Welcome to Tic-Tac-Toe!")
    boar: str = (
        "     |     |\n"
        "     |     |   \n"
        "-----|-----|-----\n"
        "     |     |   \n"
        "-----|-----|-----\n"
        "     |     |   \n"
        "     |     |"
    )
    board: list = [x for x in boar]
    sel_dict: dict = {
        "a1": 15,
        "a2": 21,
        "a3": 27,
        "b1": 49,
        "b2": 55,
        "b3": 61,
        "c1": 83,
        "c2": 89,
        "c3": 95,
    }
    select_board: str = (
        "     |     |\n"
        " a1  | a2  | a3 \n"
        "-----|-----|-----\n"
        " b1  | b2  | b3\n"
        "-----|-----|-----\n"
        " c1  | c2  | c3\n"
        "     |     |"
    )
    print(select_board)

    while counter < 9:
        if counter % 2 == 0:
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
        if counter == 9:
            print("It is a tie!")
            reset()
            break


tic_tac_toe()
