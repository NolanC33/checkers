import numpy as np

class Checkers(object):

	def draw(self):

		print(self.board)

	def reset(self):
		board = np.zeros((8, 8))

		for row in range(3):
			for col in range(8):
				if (row + col) % 2 == 1:
					board[row, col] = -1

		for row in reversed(range(5, 8)):
			for col in range(8):
				if (row + col) % 2 == 1:
					board[row, col] = 1

		self.board = board
			
	def __init__(self):
		self.reset()
		self.draw()

c = Checkers()

