import time
from aoc import *

START_TIME = time.time()

texte = read_input("input.txt")
ranges, ids = texte.split("\n\n")

R = matrix_tuples_int(ranges, sep="-")

def part1():
	res = 0
	for line in ids.splitlines():
		for a,b in R:
			if a<=int(line)<=b:
				res += 1
				break
	return res

def overlap(range1, range2):
	a,b = range1
	c,d = range2
	return a<=c<=b or c<=a<=d

def fusion(r1, r2):
	return (min(r1[0],r2[0]), max(r1[1],r2[1]))

def part2():
	E = set()
	for new_range in R:
		current_E = list(E)
		for r2 in current_E:
			if overlap(new_range,r2):
				E.remove(r2)
				new_range = fusion(new_range, r2)
		E.add(new_range)

	res = 0
	for a,b in E:
		res += b - a + 1

	return res

print("Partie 1 :", part1())
print("Partie 2 :", part2())

print(f"[{int((time.time()-START_TIME)*1000)}ms]")