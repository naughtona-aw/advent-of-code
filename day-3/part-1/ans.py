import sys
import numpy as np

def main(numbers):
	majority = len(numbers) // 2
	numbers_t = np.matrix(numbers).T
	
	gamma, epsilon = 0, 0
	for i,votes in enumerate(np.flip(numbers_t, axis=0)):
		if votes.sum() > majority:
			gamma += 2**i
		else:
			epsilon += 2**i

	return gamma * epsilon

if __name__ == "__main__":
	assert len(sys.argv) > 1

	with open(sys.argv[1],"r") as f:
		numbers = [list(map(int, line[:-1])) for line in f.readlines()]
	print(main(numbers))
