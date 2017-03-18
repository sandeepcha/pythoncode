# def draw_board():

# 	for i in range (3):
# 		row = ""
# 		for j in range (3):
# 			if (i + j) % 2 == 0:
# 				row += " b"
# 			else:
# 				row += " w"
# 		print (row)

# draw_board()

# def draw_board():
# 	print("""
# 		{0}  |  {1}  |  {2}
# 	   --------------------
# 		{3}  |  {4}  |  {5}
# 	   --------------------
# 		{6}  |  {7}  |  {8}  
# 		""".format(*board))

# board = ["X", " ", "O", "X", " ", "O", "O", " ", " "]
# draw_board()

# the function below is drawing the board
def draw_board():
	print("""
		{0}  |  {1}  |  {2}
	   --------------------
		{3}  |  {4}  |  {5}
	   --------------------
		{6}  |  {7}  |  {8}  
		""".format(*board))

def check_for_win():
	win = False
	win_combos = [
	[0, 1, 2],
	[3, 4, 5],
	[6, 7, 8],
	[0, 3, 6],
	[1, 4, 7],
	[2, 5, 8],
	[0, 4, 8],
	[2, 5, 8],
	]
	for square1, square2, square3 in win_combos:
		if board[square1] == board[square2] and board[square1] == board[square3]:
			win = board[square1]
	return win

board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
turn = "X"
draw_board()

# the loop below plays the game
while True:
	guess = "{0}'s turn to Pick a Square: " .format(turn)
	square = input (guess)
	square = int(square)
	# prevents illegal moves
	if board[square] == "X" or board[square] == "O":
		print("That space is occupied. Try again.")
		continue
	board[square] = turn
	draw_board()
	winner = check_for_win()
	print("Winner: {0}".format(winner))
	# change turn
	if turn == "X":
		turn = "O"
	else:
		turn = "X"




