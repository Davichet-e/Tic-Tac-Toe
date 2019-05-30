"""
    TODO
"""

from typing import Dict, List


def tic_tac_toe() -> None:
    counter: int = 0

    def win_condition(symbol: str) -> bool:
        return (
            board_list[15] == board_list[21] == board_list[27] == symbol
            or board_list[49] == board_list[55] == board_list[61] == symbol
            or board_list[83] == board_list[89] == board_list[95] == symbol
            or board_list[15] == board_list[49] == board_list[83] == symbol
            or board_list[21] == board_list[55] == board_list[89] == symbol
            or board_list[27] == board_list[61] == board_list[95] == symbol
            or board_list[15] == board_list[55] == board_list[95] == symbol
            or board_list[27] == board_list[55] == board_list[83] == symbol
        )

    def reset() -> bool:
        nonlocal counter
        rematch: str = input("Do you want to play again? (y/n)\n")
        if rematch.strip().lower() in ("y", "yes"):
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
            position: int = sel_dict[selection]

        except KeyError:
            print("Invalid box!")

        else:
            if board_list[position] == " ":
                board_list[position] = symbol
                counter += 1

            else:
                print("Box already selected!")

        print_board: str = "".join([char for char in board_list])

        print(print_board)

    print("Welcome to Tic-Tac-Toe!")

    board: str = (
        "     |     |\n"
        "     |     |   \n"
        "-----|-----|-----\n"
        "     |     |   \n"
        "-----|-----|-----\n"
        "     |     |   \n"
        "     |     |"
    )

    board_list: List[str] = list(board)

    sel_dict: Dict[str, int] = {
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

if __name__ == "__main__":
    tic_tac_toe()
