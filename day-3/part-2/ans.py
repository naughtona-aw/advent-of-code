import sys
import numpy as np

def main(numbers):
	def filter_values(numbers, comparator, k):
		numbers_t = np.matrix(numbers).T
		
		i = 0
		while i < numbers_t.shape[0] and numbers_t.shape[1] > 1:
			split = numbers_t.shape[1] / 2
			votes = numbers_t[i,:]
			if comparator(votes, split):
				numbers_t = np.delete(numbers_t, np.where(numbers_t[i]==0)[1], 1)
			elif numbers_t.shape[1] % 2 == 0 and votes.sum() == split:
				numbers_t = np.delete(numbers_t, np.where(numbers_t[i,:]==k)[1], 1)
			else:
				numbers_t = np.delete(numbers_t, np.where(numbers_t[i,:]==1)[1], 1)
			i += 1
		return int("0b" + "".join(map(str,numbers_t.T.tolist()[0])),2)


	ox_rating = filter_values(numbers, lambda votes, split: votes.sum() > split, 0)
	co2_rating = filter_values(numbers, lambda votes, split: votes.sum() < split, 1)
	
	return ox_rating * co2_rating

if __name__ == "__main__":
	assert len(sys.argv) > 1

	with open(sys.argv[1],"r") as f:
		numbers = [list(map(int, line[:-1])) for line in f.readlines()]
	print(main(numbers))
