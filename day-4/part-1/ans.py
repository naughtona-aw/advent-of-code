import sys, csv
import numpy as np

def main(draws, boards):
	def check_for_win(board):
		return board.all(axis=1).any() or board.all(axis=0).any()
	
	boards_m = np.array([np.full((5,5), False) for _ in range(boards.shape[0])])

	for draw in draws:
		boards_m[boards==draw] = True
		for i,board_m in enumerate(boards_m):
			if not check_for_win(board_m): continue
			
			return boards[i,~board_m].astype(int).sum() * int(draw)

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
