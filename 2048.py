import random





# Create empty board
def game_board(size):
    board = [[0] * size for _ in range(size)]
    return board


# Add a new (2 or 4) to the game board at random
def new_num_board(board):
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])


# Print current board
def print_board(board):
    for row in board:
        print(" ".join(str(cell).rjust(4) if cell != 0 else '.'.rjust(4) for cell in row))


# Move the num to the left and if there is any similar merge the both of them
def move_left(board):
    for row in board:
        row[:] = merge_tiles(row)


# If there is any merge the matching num in a row
def merge_tiles(row):
    result = [0] * len(row)
    index = 0
    for cell in row:
        if cell != 0:
            if result[index] == 0:
                result[index] = cell
            elif result[index] == cell:
                result[index] *= 2
                index += 1
            else:
                index += 1
                result[index] = cell
    return result


# (swap rows and columns)
def transpose_board(board):
    return [list(row) for row in zip(*board)]


# Move the num in the entered dir
def move(board, direction):
    if direction == 'up':
        board[:] = transpose_board(board)
        move_left(board)
        board[:] = transpose_board(board)
    elif direction == 'down':
        board[:] = transpose_board(board)
        reverse_rows(board)
        move_left(board)
        reverse_rows(board)
        board[:] = transpose_board(board)
    elif direction == 'left':
        move_left(board)
    elif direction == 'right':
        reverse_rows(board)
        move_left(board)
        reverse_rows(board)


# Reverse
def reverse_rows(board):
    for row in board:
        row.reverse()


# See if the game is finished and there is no more moves to be played 
def is_game_over(board):
    for row in board:
        if 0 in row:
            return False
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                return False
    return True


def main():
    size = 4
    board = game_board(size)
    new_num_board(board)
    new_num_board(board)

    while True:
        print_board(board)
        if is_game_over(board):
            print("Game Over! You have lost.")
            break

        direction = input("Enter a direction (up, down, left, right) or 'q' to quit: ").lower()
        if direction == 'q':
            break
        elif direction in ['up', 'down', 'left', 'right']:
            move(board, direction)
            new_num_board(board)
        else:
            print("Invalid input. Please enter a valid direction.")


if __name__ == "__main__":
    main()
