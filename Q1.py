# Do not change the code framework - you could lose your grade
# Project 1 - Q1
import os
import numpy as np


import collections

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
		self.pinput = self.processInput(rawinput)
		boxLoc = self.getBoxLocation(self.pinput)
		self.wallLoc = self.getWallLocation(self.pinput)
		self.goalLoc = self.getGoalLocation(self.pinput)
		playerLoc = self.getPlayerLocation(self.pinput)
		n_actions = self.breadthFirstSearch(boxLoc, playerLoc)

		return n_actions

	# function to help find indexes of state objects
	def findLocations(self, pinput, val):
		rows, cols = np.where(pinput==val)
		size = len(rows)
		output = np.zeros((size, 2)).astype('int')
		output[:,0] = rows
		output[:,1] = cols
		return output

	# gets location of box
	def getBoxLocation(self,pinput):
		return tuple(self.findLocations(pinput, 2)[0])
	# gets location of box
	def getPlayerLocation(self,pinput):
		return tuple(self.findLocations(pinput, 1)[0])
	# gets location of walls
	def getWallLocation(self,pinput):
		return tuple(self.findLocations(pinput, 0))
	# gets location of goal
	def getGoalLocation(self,pinput):
		return tuple(self.findLocations(pinput, 4)[0])
	# did we win the game
	def winGame(self, boxLoc):
		return (boxLoc == self.goalLoc)

	# check valid vertical moves
	def validVMoveHelper(self, move, pinput, playerLoc, boxLoc):
		newPlayerLoc = (playerLoc[0]+move, playerLoc[1])
		push = (tuple(newPlayerLoc) == tuple(boxLoc))
		try:
			if ((playerLoc[0]+move == -1)):
				return 0
			if ((push) and ((boxLoc[0]+move == -1) or (boxLoc[0]+move+move == -1))):
				return 0
			elif ((pinput[playerLoc[0]+move,playerLoc[1]] != 0)):
				if ((push) and (pinput[playerLoc[0]+move+move,playerLoc[1]] != 0)):
					return 2
				return 1
			return 0
		except:
			return 0 
		
	# check valid horizontal moves
	def validHMoveHelper(self, move, pinput, playerLoc, boxLoc):
		newPlayerLoc = (playerLoc[0], playerLoc[1]+move)
		# check if we go out of bounds with try except
		push = (tuple(newPlayerLoc) == tuple(boxLoc))
		try:
			if ((playerLoc[1]+move == -1)):
				return 0
			if ((push) and ((boxLoc[1]+move == -1) or (boxLoc[1]+move+move == -1))):
				return 0
			elif ((pinput[playerLoc[0],playerLoc[1]+move] != 0)):
				if ((push) and (pinput[playerLoc[0],playerLoc[1]+move+move] != 0)):
					return 2
				else:
					return 1
			return 0
		except:
			return 0
			
	# list of current valid moves
	def validMoves(self, playerLoc, boxLoc):
		currentValidMoves = []
		# check all four sides (up, down, left, right)
		up = self.validVMoveHelper(-1, self.pinput, playerLoc, boxLoc)
		down = self.validVMoveHelper(1, self.pinput, playerLoc, boxLoc)
		left = self.validHMoveHelper(-1, self.pinput, playerLoc, boxLoc)
		right = self.validHMoveHelper(1, self.pinput, playerLoc, boxLoc)
		if (up==1): currentValidMoves.append([-1,0,'uM'])
		if (up==2): currentValidMoves.append([-1,0,'uP'])
		if (down==1): currentValidMoves.append([1,0,'dM'])
		if (down==2): currentValidMoves.append([1,0,'dP'])
		if (left==1): currentValidMoves.append([0,-1,'lM'])
		if (left==2): currentValidMoves.append([0,-1,'lP'])
		if (right==1): currentValidMoves.append([0,1,'rM'])
		if (right==2): currentValidMoves.append([0,1,'rP'])
		return currentValidMoves
	
	# update location of player and box based on action
	def updateLocations(self, playerLoc, boxLoc, currentAction):
		newPlayerLoc = playerLoc[0]+currentAction[0], playerLoc[1]+currentAction[1]
		if (currentAction[2][1] == 'P'):
			boxLoc = (boxLoc[0]+currentAction[0], boxLoc[1]+currentAction[1])
		return newPlayerLoc, boxLoc
		
	
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

	# BFS implementation
	def breadthFirstSearch(self, boxLoc, playerLoc):
		beginBox = boxLoc
		beginPlayer = playerLoc

		startState = (beginPlayer, beginBox) # e.g. ((2, 2), ((2, 3), (3, 4), (4, 4), (6, 1), (6, 4), (6, 5)))
		frontier = collections.deque([[startState]]) # store states
		actions = collections.deque([[0]]) # store actions
		exploredSet = set()

		while frontier:
			node = frontier.popleft()
			node_action = actions.popleft() 
			if self.winGame(node[-1][-1]):
				return len(node_action[1:])
			if node[-1] not in exploredSet:
				exploredSet.add(node[-1])
				for action in self.validMoves(node[-1][0], node[-1][1]):
					newPosPlayer, newPosBox = self.updateLocations(node[-1][0], node[-1][1], action)
					frontier.append(node + [(newPosPlayer, newPosBox)])
					actions.append(node_action + [action[-1]])
		# failed -> couldn't find solution
		return -1

if __name__=='__main__':
	test_file_number = 5 # Change this to use different test files
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