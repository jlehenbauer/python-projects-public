import time
def tic_tac_toe():
	board = [[' 1 ',' 2 ',' 3 '],[' 4 ',' 5 ',' 6 '],[' 7 ',' 8 ',' 9 ']]
	player_X = [-1, -1]
	player_O = [-1, -1]
	moves = 0

	print("Welcome to Tic-Tac-Toe!")
	while moves <= 9:
		# Show where we are and check
		# to see if anyone's one before
		# we accept more moves
		print_board(board)
		if check_for_winner(board):
			print("Congratulations!")
			return True

		# Start player 1's turn
		print("X, select your move!")
		trying = 1
		while trying == 1:
			player_X = player_turn(player_X)
			if board[player_X[0]][player_X[1]] == ' X ' or board[player_X[0]][player_X[1]] == ' O ':
				print("Please make another selection")
			else:
				trying = 0

		board[player_X[0]][player_X[1]] = ' X '
		moves += 1

		# If we're done or need to check for a winner,
		# do so now
		if moves >= 9:
			break
		elif moves > 4:
			if check_for_winner(board):
				print_board(board)
				print("Congratulations!")
				return True

		# Update board view
		print_board(board)

		# Start player 2's turn
		print("O, select your move!")
		trying = 1
		while trying == 1:
			player_O = player_turn(player_O)
			if board[player_O[0]][player_O[1]] == ' X ' or board[player_O[0]][player_O[1]] == ' O ':
				print("Please make another selection")
			else:
				trying = 0

		board[player_O[0]][player_O[1]] = ' O '
		moves += 1

		print(moves)

	if check_for_winner(board):
		print_board(board)
		print("Congratulations!")
		return True


	print("It's a tie!")
	print("Game Over!")
	print_board(board)
	return False


def print_board(board):
	print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
	print("--- | --- | ---")
	time.sleep(.4)
	print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
	print("--- | --- | ---")
	time.sleep(.4)
	print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])
	print()
	print()
	time.sleep(1)
	return True

def check_for_winner(board):
	for row in board:
		if row[0] == row[1] == row[2]:
			print(str(row[1]) + " wins!")
			return True

	for col in range(len(board)):
		if board[0][col] == board[1][col] == board[2][col]:
			print(str(board[1][col]) + " wins!")
			return True

	if board[0][0] == board[1][1] == board[2][2]:
		print(str(board[1][1]) + " wins!")
		return True

	elif board[0][2] == board[1][1] == board[2][0]:
		print(str(board[1][1]) + " wins!")
		return True

	return False

def player_turn(player):
	selection = int(input("Choose 1 - 9: "))
	print()
	if selection < 1 or selection > 9:
		return [-1, -1]
	player[0] = (selection - 1) // 3
	player[1] = (selection + 2) % 3 
	return player

tic_tac_toe()
