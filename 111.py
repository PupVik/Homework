table = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def view_board(board):
    for row in board:
        for cell in row:
            print(cell, end = " ")
        print()

def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i]:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if  board[0][2] == player and board[1][1] == [player] and board[2][0] == player:
        return True

player_1 = "x"

while True:
    view_board(table)
    print('ход игрока', player_1)
    row = int(input("ведите номер строки: ")) - 1
    col = int(input("ведите номер столбца: ")) - 1

    if table[row][col] != " ":
        print("Ячейка занята")
        continue

    table[row][col] = player_1

    if check_win(table, player_1):
        view_board(table)
        print(f"Игрок {player_1} победил")
        break

    if all([cell != " " for row in table for cell in row]):
        print("Ничья")
        view_board
        break

    player_1 = "0" if player_1 == "x" else "x"






