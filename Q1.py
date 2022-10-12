# Do not change the code framework - you could lose your grade
# Project 1 - Q1
import os
import numpy as np
import sys
class SokubanSolver1:
	def __loadInput(self, filename):
		f = open(filename, 'r')
		rawinput = []
		for line in f.readlines():
			rawinput.append(line.strip())
		return rawinput

	def solve(self, inputFilename): 
		rawinput = self.__loadInput(inputFilename)
		# Implement this
		# Start with processing the input, get the initial state and game map 
		pinput = self.processInput(rawinput)
		print(pinput)
		boxLoc = self.getBoxLocation(pinput)
		wallLoc = self.getWallLocation(pinput)
		playerLoc = self.getPlayerLocation(pinput)
		self.validMoves(pinput, playerLoc, boxLoc)
		sys.exit()
		# Then implement a search function
		solution = -1 # Change this
		return solution

	# cleans up np.where operation
	def findLocations(self, pinput, val):
		rows, cols = np.where(pinput==val)
		size = len(rows)
		output = np.zeros((size, 2)).astype('int')
		output[:,0] = rows
		output[:,1] = cols

		return output

	# gets location of box
	def getBoxLocation(self,pinput):
		return self.findLocations(pinput, 2)[0]
	# gets location of box
	def getPlayerLocation(self,pinput):
		return self.findLocations(pinput, 1)[0]
	# gets location of walls
	def getWallLocation(self,pinput):
		return self.findLocations(pinput, 0)
	# gets location of goal
	def getGoalLocation(self,pinput):
		return self.findLocations(pinput, 4)[0]
	# check valid vertical moves
	def validVMoveHelper(self, move, pinput, playerLoc, boxLoc):
		if ((pinput[playerLoc[0]+move,playerLoc[1]] == 3) or (pinput[playerLoc[0]+move,playerLoc[1]] == 4)):
			return 1
		elif ((pinput[playerLoc[0]+move,playerLoc[1]] == 2) and (pinput[playerLoc[0]+move+move,playerLoc[1]] != 0)):
			return 2
		return 0
	# check valid horizontal moves
	def validHMoveHelper(self, move, pinput, playerLoc, boxLoc):
		if ((pinput[playerLoc[0],playerLoc[1]+move] == 3) or (pinput[playerLoc[0],playerLoc[1]+move] == 4)):
			return 1
		elif ((pinput[playerLoc[0],playerLoc[1]+move] == 2) and (pinput[playerLoc[0],playerLoc[1]+move+move] != 0)):
			return 2
		return 0
	# list of current valid moves
	def validMoves(self, pinput, playerLoc, boxLoc):
		currentValidMoves = []
		# check all four sides (up, down, left, right)
		up = self.validVMoveHelper(-1, pinput, playerLoc, boxLoc)
		down = self.validVMoveHelper(1, pinput, playerLoc, boxLoc)
		left = self.validHMoveHelper(-1, pinput, playerLoc, boxLoc)
		right = self.validHMoveHelper(1, pinput, playerLoc, boxLoc)
		if (up==1): currentValidMoves.append([-1,0,'u'])
		if (up==2): currentValidMoves.append([-1,0,'uP'])
		if (down==1): currentValidMoves.append([1,0,'d'])
		if (down==2): currentValidMoves.append([1,0,'dP'])
		if (left==1): currentValidMoves.append([0,-1,'l'])
		if (left==2): currentValidMoves.append([0,-1,'lP'])
		if (right==1): currentValidMoves.append([0,1,'r'])
		if (right==2): currentValidMoves.append([0,1,'rP'])
		return currentValidMoves
	
	def updateLocations(self, playerLoc, boxLoc, currentAction):
		currentPX, currentPY = playerLoc
		playerLoc = currentPX+currentAction[0], currentPY+currentAction[1]
		if (currentAction[2][1] == 'P'):
			boxLoc = [boxLoc[0]+currentAction[0], boxLoc[1]+currentAction[1]]
		return playerLoc, boxLoc
		
	def processInput(self, rawinput):
		dim0 = len(rawinput[0])
		dim1 = len(rawinput)
		output = np.zeros((dim1,dim0)).astype('int')
		for i in range(dim1):
			for j in range(dim0):
				if (rawinput[i][j] == '#'):
					output[i][j] = 0
				elif (rawinput[i][j] == 'P'):
					output[i][j] = 1
				elif (rawinput[i][j] == 'B'):
					output[i][j] = 2
				elif (rawinput[i][j] == '.'):
					output[i][j] = 3
				elif (rawinput[i][j] == '*'):
					output[i][j] = 4
		return output


if __name__=='__main__':
	test_file_number = 3 # Change this to use different test files
	filename = 'game%d.txt' % test_file_number
	testfilepath = os.path.join('test','Q1', filename)
	Solver = SokubanSolver1()
	res = Solver.solve(testfilepath)

	ansfilename = 'ans%d.txt' % test_file_number 
	answerfilepath = os.path.join('test', 'Q1', ansfilename)
	f = open(answerfilepath, 'r')
	ans = int(f.readlines()[0].strip())

	print('Your answer is %d. True answer is %d.' % (res, ans))

	if res == ans:
		print('Answer is correct.')
	else:
		print('Answer is wrong.')