# Initiate time
import time

# Create class of tic-tac-toe game
class Game:
	def __init__(self):
		# Call initialize_game function
		self.initialize_game()

	# Create initialize game function of empty 3x3 array
	def initialize_game(self):
		self.current_state = [['.','.','.'],
							  ['.','.','.'],
							  ['.','.','.']]

		# Player X always plays first
		self.player_turn = 'X'

	# Draw board by using print to show the output of each element of current_state
	def draw_board(self):
		for i in range(0, 3):
			for j in range(0, 3):
				print('{}|'.format(self.current_state[i][j]), end=" ")
			# Enter down after print complete row ".| .| .|"
			print()
		# Provide one empty line
		print()

	# Determines if the made move is a legal move
	def is_valid(self, px, py):
		# If the giving position x or y is not in range [0, 2]
		# return False (Code error)
		if px < 0 or px > 2 or py < 0 or py > 2:
			return False
		# and if current input is already used
		# return False 
		elif self.current_state[px][py] != '.':
			return False
		# otherwise, the input is valid
		else:
			return True

	# Checks if the game has ended and returns the winner in each case
	# TicTacToe game has 3 condition to be winner
	# 1. Any column with same symbol
	# 2. Any row with same symbol
	# 3. Any diagnal with same symbol
	def is_end(self):
		# 1. Any column with same symbol
		# Check each column whether each block has same symbol 
		for i in range(0, 3):
			if (self.current_state[0][i] != '.' and
				self.current_state[0][i] == self.current_state[1][i] and
				self.current_state[1][i] == self.current_state[2][i]):
				return self.current_state[0][i]

		# 2. Any row with same symbol
		# Check each row whether each block has same symbol 
		for i in range(0, 3):
			if (self.current_state[i] == ['X', 'X', 'X']):
				return 'X'
			elif (self.current_state[i] == ['O', 'O', 'O']):
				return 'O'

		# Main diagonal win
		# Check 1st diagonal whether each block has same symbol 
		if (self.current_state[0][0] != '.' and
			self.current_state[0][0] == self.current_state[1][1] and
			self.current_state[0][0] == self.current_state[2][2]):
			return self.current_state[0][0]

		# Second diagonal win
		# Check 2nd diagonal whether each block has same symbol
		if (self.current_state[0][2] != '.' and
			self.current_state[0][2] == self.current_state[1][1] and
			self.current_state[0][2] == self.current_state[2][0]):
			return self.current_state[0][2]

		# Is whole board full?
		for i in range(0, 3):
			for j in range(0, 3):
				# There's an empty field, we continue the game
				if (self.current_state[i][j] == '.'):
					return None

		# It's a tie!
		return '.'

	# Player 'O' is min, in this case AI
	def min(self):

		# Possible values for minv are:
		# -1 - win
		# 0  - a tie
		# 1  - loss

		# We're initially setting it to 2 as worse than the worst case:
		minv = 2

		qx = None
		qy = None

		result = self.is_end()

		if result == 'O':
			return (-1, 0, 0)
		elif result == 'X':
			return (1, 0, 0)
		elif result == '.':
			return (0, 0, 0)

		for i in range(0, 3):
			for j in range(0, 3):
				if self.current_state[i][j] == '.':
					self.current_state[i][j] = 'O'
					(m, max_i, max_j) = self.max()
					if m < minv:
						minv = m
						qx = i
						qy = j
					self.current_state[i][j] = '.'

		return (minv, qx, qy)
		
	# Player 'X' is max, in this case human
	def max(self):

		# Possible values for maxv are:
		# -1 - loss
		# 0  - a tie
		# 1  - win

		# We're initially setting it to -2 as worse than the worst case:
		maxv = -2

		px = None
		py = None

		result = self.is_end()

		# If the game came to an end, the function needs to return
		# the evaluation function of the end. That can be:
		# -1 - loss
		# 0  - a tie
		# 1  - win
		if result == 'O':
			return (-1, 0, 0)
		elif result == 'X':
			return (1, 0, 0)
		elif result == '.':
			return (0, 0, 0)

		for i in range(0, 3):
			for j in range(0, 3):
				if self.current_state[i][j] == '.':
					# On the empty field player 'X' makes a move and calls Min
					# That's one branch of the game tree.
					self.current_state[i][j] = 'X'
					(m, min_i, min_j) = self.min()
					# Fixing the maxv value if needed
					if m > maxv:
						maxv = m
						px = i
						py = j
					# Setting back the field to empty
					self.current_state[i][j] = '.'
		return (maxv, px, py)

	def play(self):
		while True:
			self.draw_board()
			self.result = self.is_end()

			# Printing the appropriate message if the game has ended
			if self.result != None:
				if self.result == 'X':
					print('The winner is X!')
				elif self.result == 'O':
					print('The winner is O!')
				elif self.result == '.':
					print("It's a tie!")

				self.initialize_game()
				return

			# If it's player's turn
			if self.player_turn == 'X':

				while True:

					start = time.time()
					(m, px, py) = self.max()
					end = time.time()
					print('Evaluation time: {}s'.format(round(end - start, 7)))
					print('Recommended move: X = {}, Y = {}'.format(px, py))

					qx = int(input('Insert the X coordinate: '))
					qy = int(input('Insert the Y coordinate: '))

					(px, py) = (qx, qy)

					if self.is_valid(qx, qy):
						self.current_state[qx][qy] = 'X'
						self.player_turn = 'O'
						break
					else:
						print('The move is not valid! Try again.')

			# If it's AI's turn
			else:
				(m, qx, qy) = self.min()
				self.current_state[qx][qy] = 'O'
				self.player_turn = 'X'

def main():
	g = Game()
	g.play()

if __name__ == "__main__":
	main()