import sys

def main(measurements):
	return sum(1 for i,x in enumerate(measurements[1:]) if x > measurements[i])

if __name__ == "__main__":
	assert len(sys.argv) > 1

	with open(sys.argv[1],"r") as f:
		measurements = [int(line) for line in f.readlines()]
	print(main(measurements))
