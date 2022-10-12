# Do not change the code framework - you could lose your grade
# Project 1 - Q1
import os

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
		# Then implement a search function
		solution = -1 # Change this
		return solution


if __name__=='__main__':
	test_file_number = 1 # Change this to use different test files
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