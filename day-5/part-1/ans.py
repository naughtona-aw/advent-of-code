import sys
import numpy as np

def main(segs, maxy, maxx):
	def mark_area(seg, area):
		indices = []
		(x1,x2), (y1,y2) = zip(*seg)
		
		if x1 == x2:
			l, h = (y2,y1) if y1 > y2 else (y1,y2)
			indices += list(range(l-1,h))
			area[indices, x1-1] += 1
		elif y1 == y2:
			l, h = (x2,x1) if x1 > x2 else (x1,x2)
			indices += list(range(l-1,h))
			area[y1-1, indices] += 1

	area = np.zeros((maxy,maxx))
	for seg in segs:
		mark_area(seg, area)

	return (area >= 2).sum()

if __name__ == "__main__":
	assert len(sys.argv) > 1

	with open(sys.argv[1],"r") as f:
		segs, maxx, maxy = [], 0, 0
		for i,line in enumerate(f.readlines()):
			segs.append([])
			for pt in line[:-1].split(" -> "):
				x, y = map(int, pt.split(","))
				segs[i] += ((x, y),)
				if x > maxx:
					maxx = x
				if y > maxy:
					maxy = y

	print(main(segs, maxy, maxx))
