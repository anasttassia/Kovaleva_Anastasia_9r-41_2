import random

def print_board(board):
    print("  1   2   3")
    print("  " + "-" * 11)

    for i, row in enumerate(board, 1):
        # Преобразуем строку доски для отображения
        row_display = []
        for cell in row:
            if cell == "X":
                row_display.append("X")
            elif cell == "O":
                row_display.append("O")
            else:
                row_display.append(" ")

        print(f"{i}  {row_display[0]} | {row_display[1]} | {row_display[2]} ")
        if i < 3:
            print("  " + "-" * 11)

def check_winner(board):
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Проверка диагоналей
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

def play_game():
    # Инициализация пустой доски
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    
    current_player = "X"
    
    print("\n" + "=" * 40)
    print("  КРЕСТИКИ-НОЛИКИ")
    print("=" * 40)
    print("Игрок 1: X (Крестики)")
    print("Игрок 2: O (Нолики)")
    print("\n Как ходить: введите два числа (строка и столбец)")
    print("Например: '2 3' для второй строки, третьего столбца")
    print("=" * 40)
    
    while True:
        # Показываем доску
        print(f"\n Ход игрока: {current_player}")
        print_board(board)
        
        # Получаем ход от игрока
        while True:
            try:
                move = input(f"\nИгрок {current_player}, ваш ход (строка столбец): ").strip()
                
                if not move:
                    print("Введите что-нибудь!")
                    continue
                    
                # Разбиваем ввод
                parts = move.split()
                if len(parts) != 2:
                    print("Нужно ввести ДВА числа через пробел!")
                    continue
                
                row, col = int(parts[0]), int(parts[1])
                
                # Проверяем границы
                if not (1 <= row <= 3) or not (1 <= col <= 3):
                    print("Координаты должны быть от 1 до 3!")
                    continue
                
                # Преобразуем в индексы массива
                row_idx = row - 1
                col_idx = col - 1
                
                # Проверяем, свободна ли клетка
                if board[row_idx][col_idx] != " ":
                    print("Эта клетка уже занята!")
                    continue
                
                # Ход корректный
                break
                
            except ValueError:
                print("Ошибка! Введите числа, например: '2 3'")
                continue
            except KeyboardInterrupt:
                print("\nИгра прервана!")
                return
        
        # Ставим символ на доску
        board[row_idx][col_idx] = current_player
        
        # Проверяем победу
        winner = check_winner(board)
        if winner:
            print_board(board)
            print("\n" + "=" * 40)
            print(f"  ПОБЕДА! Игрок {winner} выиграл!")
            print("=" * 40)
            break
        
        # Проверяем ничью
        if is_board_full(board):
            print_board(board)
            print("\n" + "=" * 40)
            print(f"  НИЧЬЯ!")
            print("=" * 40)
            break
        
        # Меняем игрока
        current_player = "O" if current_player == "X" else "X"

# Запуск игры
if __name__ == "__main__":
    play_game()

