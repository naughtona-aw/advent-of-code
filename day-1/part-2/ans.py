import sys

def main(measurements):
	sum3 = lambda last_index: sum(measurements[last_index-2:last_index+1])
	return sum(1 for i in range(3,len(measurements)) if sum3(i)  > sum3(i-1))

if __name__ == "__main__":
	assert len(sys.argv) > 1

	with open(sys.argv[1],"r") as f:
		measurements = [int(line) for line in f.readlines()]
	print(main(measurements))
