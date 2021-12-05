import sys, csv
import numpy as np

def main(draws, boards):
	def check_for_win(board):
		return board.all(axis=1).any() or board.all(axis=0).any()
	
	boards_m = np.array([np.full((5,5), False) for _ in range(boards.shape[0])])
	incomplete = list(range(boards.shape[0]))

	i = 0; last = None
	while i < len(draws) and len(incomplete) > 0:
		boards_m[boards==draws[i]] = True
		for j in incomplete:
			if not check_for_win(boards_m[j]): continue

			incomplete.remove(j)
			last = j
		i += 1

	return boards[last,~boards_m[last]].astype(int).sum() * int(draws[i-1])

if __name__ == "__main__":
	assert len(sys.argv) > 1

	with open(sys.argv[1],"r") as f:
		csv_reader = csv.reader(f)
		draws = next(csv_reader)

		i, boards = -1, []
		for line in csv_reader:
			if not line:
				boards.append([])
				i += 1
			else:
				boards[i].append(line[0].split())

		boards = np.array(boards)
	
	print(main(draws, boards))
