# Do not change the code framework - you could lose your grade
# Project 1 - Q2
import os
import heapq 
# You can use the heapq library in python standard libraries to implement priority queues.
# Check the Python doc of heapq.heappop and heapq.heappush at https://docs.python.org/3/library/heapq.html

class SokubanSolver2:
	def __loadInput(self, filename):
		f = open(filename, 'r')
		rawinput = []
		for line in f.readlines():
			rawinput.append(line.strip())
		return rawinput

	def heuristic(self, state, target):
		# Implement this
		return 0

	def solve(self, inputFilename): 
		rawinput = self.__loadInput(inputFilename)
		# Implement this
		# Start with processing the input, get the initial state and game map - You can reuse what you did in Q1
		# Then implement the heuristic function above
		# Finally, implement the A* algorithm
		solution = -1 # Change this
		return solution


if __name__=='__main__':
	test_file_number = 1 # Change this to use different test files
	filename = 'game%d.txt' % test_file_number
	testfilepath = os.path.join('test','Q2', filename)
	Solver = SokubanSolver2()
	res = Solver.solve(testfilepath)

	ansfilename = 'ans%d.txt' % test_file_number 
	answerfilepath = os.path.join('test', 'Q2', ansfilename)
	f = open(answerfilepath, 'r')
	ans = int(f.readlines()[0].strip())

	print('Your answer is %d. True answer is %d.' % (res, ans))

	if res == ans:
		print('Answer is correct.')
	else:
		print('Answer is wrong.')