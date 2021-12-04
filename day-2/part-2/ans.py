import sys

HORIZ = {"forward": 1}
DEPTH = {"up": -1, "down": 1}

def main(directions):
	x, y, aim = 0, 0, 0

	for dir,dist in directions:
		if dir in HORIZ:
			x += HORIZ[dir] * int(dist)
			y += int(dist) * aim
		elif dir in DEPTH:
			aim += DEPTH[dir] * int(dist)

	return x * y

if __name__ == "__main__":
	assert len(sys.argv) > 1

	with open(sys.argv[1],"r") as f:
		directions = [line.split() for line in f.readlines()]
	print(main(directions))
