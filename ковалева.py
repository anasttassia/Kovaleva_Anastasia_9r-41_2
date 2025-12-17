import random


def print_board(board):
    print("  1   2   3")
    print("  " + "-" * 11)

    for i, row in enumerate(board, 1):
        row_display = []
        for cell in row:
            if cell == "X":
                row_display.append("X")
            elif cell == "O":
                row_display.append("O")
            else:
                row_display.append(" ")

        print(f"{i}| {row_display[0]} | {row_display[1]} | {row_display[2]} |")
        if i < 3:
            print("  " + "-" * 11)


def get_symbol(symbol):
    return symbol


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells


def computer_move(board, computer_symbol):
    empty_cells = get_empty_cells(board)

    for row, col in empty_cells:
        board[row][col] = computer_symbol
        if check_winner(board) == computer_symbol:
            board[row][col] = " "
            return row, col
        board[row][col] = " "

    player_symbol = "X" if computer_symbol == "O" else "O"
    for row, col in empty_cells:
        board[row][col] = player_symbol
        if check_winner(board) == player_symbol:
            board[row][col] = " "
            return row, col
        board[row][col] = " "

    if (1, 1) in empty_cells:
        return 1, 1

    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [
        corner for corner in corners if corner in empty_cells
    ]
    if available_corners:
        return random.choice(available_corners)

    return random.choice(empty_cells)


def play_with_friend():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("\n" + "=" * 40)
    print("  РЕЖИМ: ИГРА С ДРУГОМ")
    print("=" * 40)
    print(f"Игрок 1: X (Крестики)")
    print(f"Игрок 2: O (Нолики)")

    while True:
        symbol = get_symbol(current_player)
        print(f"\nСейчас ходит: Игрок [{symbol}]")
        print_board(board)

        try:
            coords = input("\nХод игрока (строка столбец): ").strip().split()

            if len(coords) != 2:
                print("Ошибка! Нужно ввести ДВА числа через пробел")
                continue

            row, col = map(int, coords)

            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Ошибка! Координаты должны быть от 1 до 3")
                continue

            row -= 1
            col -= 1

            if board[row][col] != " ":
                print("Эта клетка уже занята! Выберите другую.")
                continue

        except ValueError:
            print("Ошибка! Введите числа, например: '2 3'")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            winner_symbol = get_symbol(winner)
            print_board(board)
            print(f" Победа! Игрок [{winner_symbol}] выиграл! ")
            break

        if is_board_full(board):
            print_board(board)
            print(f" Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"


def play_with_computer():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("\n" + "=" * 40)

