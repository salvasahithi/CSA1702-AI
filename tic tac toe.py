def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def is_valid_move(move):
    return move.isdigit() and 1 <= int(move) <= 9

def apply_move(board, move, player):
    row = (int(move) - 1) // 3
    col = (int(move) - 1) % 3

    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        return False

def switch_player(player):
    return 'O' if player == 'X' else 'X'

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")

        if not is_valid_move(move):
            print("Invalid move. Please enter a number from 1 to 9.")
            continue

        if not apply_move(board, move, current_player):
            print("Invalid move. That spot is already taken.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = switch_player(current_player)

if __name__ == "__main__":
    play_tic_tac_toe()
